from enum import Enum

class ICCError(Enum):
    def __init__(self, error_code, error_message):
        super().__init__()
        self.error_code = error_code
        self.error_message = error_message



class CustomICCError(ICCError):
    UNAUTHORIZED = (401, "Unauthorized")
    USER_NOT_FOUND = (404, "User not found")
    USERS_NOT_FOUND = (404, "Users not found")
    GOOGLE_AUTHENTICATION_FAILED = (400, "Google Authentication Failed")
    INVALID_PARAMS_OR_REQUIRED_PARAMS_MISSING = (422, "Invalid params or required params missing")
    PRODUCT_NOT_FOUND = (404, "Product not found")

    #otp
    SENDING_OTP_FAILED_PLEASE_TRY_AGAIN_LATER = (400, "Unable to send otp, Please try again later.")
    OTP_NOT_FOUND_PLEASE_SEND_OTP_FIRST = (400, "Otp verification failed, please send otp before verifying")
    OTP_VERIFICATION_FAIELD = (400, "Incorrect Otp Entered. Please try Again!")
    
    #admin login
    ADMIN_NOT_FOUND = (404, "Admin not found")