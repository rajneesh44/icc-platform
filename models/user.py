from enum import IntEnum
from core.entity import Entity
from utils.util import generate_referral_code
from pydantic import Field

class UserType(IntEnum):
    ICC_FAN = 0
    ICC_ADMIN = 1


class User(Entity):
    name: str = None
    email: str = None
    phone_number: str = None
    user_name: str = None
    user_type: int = UserType.ICC_FAN
    coins_earned: int = 0
    profile_img_url: str = ""
    referral_code: str = Field(default_factory=generate_referral_code)


