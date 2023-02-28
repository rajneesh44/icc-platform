from enum import Enum

class ICCError(Enum):
    def __init__(self, error_code, error_message):
        super().__init__()
        self.error_code = error_code
        self.error_message = error_message



class CustomICCError(ICCError):
    UNKNOWN_ERROR = (100, "Something went wrong")
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

    #CART
    CART_NOT_FOUND = (404, "No Items in cart or Cart is Empty")
    CAN_NOT_REMOVE_FROM_CART = (400, "Can not remove item/items from cart. Please try again later")
    CART_ALREADY_EMPTY = (200, "Cart is already Empty")

    #Address
    ADDRESS_NOT_FOUND = (404, "Address Not found")

    #REFERRAL
    INVALID_REFERRAL_CODE = (400, "Invalid referral code")
    REFERRAL_CODE_ERROR = (400, "Referral code error")