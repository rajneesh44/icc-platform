from instamojo_wrapper import Instamojo
import os

API_KEY = os.getenv("INSTAMOJO_PRIVATE_API_KEY")
AUTH_TOKEN = os.getenv("INSTAMOJO_PRIVATE_AUTH_TOKEN")

api = Instamojo(api_key=API_KEY,auth_token=AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')


class InstaMojoController:
    @staticmethod
    def create_payment_request(amount: float, purpose: str, send_email=False, email=None, send_sms=False, phone_number=False):
        response = api.payment_request_create(
            amount=amount,
            purpose=purpose,
            send_email=send_email,
            email=email,
            send_sms=send_sms,
            phone=phone_number,
            # redirect_url="http://www.example.com/handle_redirect.py"
            )
        
        print('=====>', response)
        print(response['payment_request']['longurl'])
        print(response['payment_request']['id'])
        return response["payment_request"]
    
    @staticmethod
    def check_payment_status(payment_id):
        response = api.payment_request_status(payment_id)
        return response["payment_request"]["status"]

    @staticmethod
    def get_all_payments():
        response = api.payment_requests_list()
        return [payment for payment in response["payment_requests"]]