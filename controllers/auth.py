import os
import logging
from google.oauth2 import id_token
from google.auth.transport import requests
from utils.login import login_user
from dotenv import load_dotenv
from utils.error import CustomICCError
from controllers.user import UserController
from controllers.sms_provider_controller import Fast2SMSController
from random import randint
from models.otp_info import OtpInfo
from time import time
import random
import bcrypt


load_dotenv()
uc = UserController()

CLIENT_ID = os.getenv("CLIENT_ID")
PASSWORD_SALT = os.getenv("PASSWORD_SALT")

class AuthController:
    def google_auth_callback(self, token: str):
        try:
            info = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)            
            email = info["email"]
            name = info['given_name']   + " "   + info.get('family_name',"")
            profile_img_url = info.get("picture", "")

            user_obj = {
                "email": email,
                "name": name,
                "profile_img_url": profile_img_url
            }
            user = uc.find_user({"email": email})
            if not user or isinstance(user, CustomICCError):
                user = uc.create_user(user_obj)
            if user:
                login_user(user)
            return user
    
        except Exception as e:
            logging.info(e.__dict__)
            return CustomICCError.GOOGLE_AUTHENTICATION_FAILED
        

    def send_otp(self, phone: str):
        otp = int(random.randint(100000, 999999))
        message = f"Your OTP for Login is {otp}. Otp will be valid for 10 minutes."
        otp_info = OtpInfo.find_one({"phone": phone, "status": 0})
        if otp_info:
            if int(otp_info.updated_at) + 30 >= int(time()):
                return CustomICCError.SENDING_OTP_FAILED_PLEASE_TRY_AGAIN_LATER
            else:
                otp_info.otp= otp
                otp_info.expiration_time = int(time()) + 60*10
                otp_info.update()
        else:
            otp_dict = {
                "phone": phone,
                "otp": otp,
            }
            otp_info = OtpInfo.from_dict(otp_dict)
            otp_info.update()
        try:
            Fast2SMSController.send_otp(phone, message)
        except:
            return CustomICCError.SENDING_OTP_FAILED_PLEASE_TRY_AGAIN_LATER
        return True

    def verify_otp(self, phone: str, otp: int):
        otp_info = OtpInfo.find_one({"phone": phone, "status": 0})
        if not otp_info:
            return CustomICCError.OTP_NOT_FOUND_PLEASE_SEND_OTP_FIRST
        if int(otp_info.otp) == otp and otp_info.expiration_time > int(time()):
            otp_info.status = 2
            otp_info.update()

            user = uc.find_user({"phone_number": phone})
            if not user or isinstance(user, CustomICCError):
                user_obj = {"phone_number": phone}
                user = uc.create_user(user_obj)
            if user:
                login_user(user)
            return user
        else:
            return CustomICCError.OTP_VERIFICATION_FAIELD
        
    def login_admin_with_password(self, username: str, password: str):
        encoded_password = password.encode("utf-8")
        encoded_salt = PASSWORD_SALT.encode("utf-8")
        encrypted_password = bcrypt.hashpw(encoded_password, encoded_salt)
        user = uc.find_user({"email": username, "password": encrypted_password.decode("utf-8")})
        if not user or isinstance(user, CustomICCError):
            return CustomICCError.ADMIN_NOT_FOUND
        user["password"] = None
        login_user(user)
        return user
