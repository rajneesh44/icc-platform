from enum import IntEnum
from core.entity import Entity
from utils.util import generate_referral_code
from dataclasses import dataclass, field

class UserType(IntEnum):
    ICC_FAN = 0
    ICC_ADMIN = 1


@dataclass
class User(Entity):
    name: str = None
    email: str = None
    phone_number: str = None
    user_name: str = None
    user_type: int = UserType.ICC_FAN
    coins_earned: int = 0
    profile_img_url: str = ""
    referral_code: str = field(default_factory=generate_referral_code)
    fcm: str = None
    password: str = None


