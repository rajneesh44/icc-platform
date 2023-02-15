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

load_dotenv()
uc = UserController()

CLIENT_ID = os.getenv("CLIENT_ID")


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
        otp = int(''.join(["{}".format(randint(0, 9)) for num in range(0, 6)]))
        message = f"Your OTP for Login is {otp}. Otp will be valid for 10 minutes."
        otp_info = OtpInfo.find_one({"phone": phone, "status": 0})
        if otp_info:
            if int(otp_info.updated_at) + 30 >= int(time()):
                return CustomICCError.SENDING_OTP_FAILED_PLEASE_TRY_AGAIN_LATER
            else:
                otp_info.otp= otp
                otp_info.update()
        if not otp_info:
            otp_dict = {
                "phone": phone,
                "otp": otp,
            }
            otp_info = OtpInfo.parse_obj(otp_dict)
            otp_info.update()

        Fast2SMSController.send_otp(phone, message)
        return True

    def verify_otp(self, phone: str, otp: int):
        otp_info = OtpInfo.find_one({"phone": phone, "otp": otp, "status": 0})
        if not otp_info:
            return CustomICCError.OTP_NOT_FOUND_PLEASE_SEND_OTP_FIRST
        print(otp_info.expiration_time, time(), otp, otp_info.__dict__)
        if int(otp_info.otp) == otp and otp_info.expiration_time > int(time()):
            otp_info.status = 2
            otp_info.update()

            user = uc.find_user({"phone": phone})
            if not user or isinstance(user, CustomICCError):
                user_obj = {"name": phone, "phone": phone}
                user = uc.create_user(user_obj)
            if user:
                login_user(user)
            return user
        else:
            return CustomICCError.OTP_VERIFICATION_FAIELD
        

            
