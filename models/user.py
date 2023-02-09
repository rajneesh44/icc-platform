from dataclasses import dataclass, field
from enum import IntEnum
from core.entity import Entity
import random


class UserType(IntEnum):
    ICC_FAN = 0
    ICC_ADMIN = 1


@dataclass
class User(Entity):
    name: str = None
    email: str = None
    phone_number: str = None
    user_name: str = None
    user_type: UserType = UserType.ICC_FAN
    coins_earned: int = 0
    profile_img_url: str = ""
    # referral_code: str = field(default_factory=generate_referral_code)



# def generate_referral_code(self):
#     code = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(6))
#     return code