import os
import requests
from dotenv import load_dotenv

load_dotenv()

FAST2SMS_API_KEY = os.getenv("FAST2SMS_API_KEY")

class Fast2SMSController:
    @staticmethod
    def send_otp(phone: str, message: str):
        base_url = f'https://www.fast2sms.com/dev/bulkV2?authorization={FAST2SMS_API_KEY}&route=v3&sender_id=ICCSBP&message={message}&language=english&flash=0&numbers={phone}'
        response = requests.get(base_url)
        return response.text
    