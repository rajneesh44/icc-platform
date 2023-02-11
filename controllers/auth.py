import os
import logging
from google.oauth2 import id_token
from google.auth.transport import requests
from utils.login import login_user
from dotenv import load_dotenv
from utils.error import CustomICCError
from controllers.user import UserController

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
            if not user:
                user = uc.create_user(user_obj)
                
            login_user(user)
            return user
        
        except Exception as e:
            logging.info(e.__dict__)
            return CustomICCError.UNAUTHORIZED
        
