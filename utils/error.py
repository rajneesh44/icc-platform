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