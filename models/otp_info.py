from enum import IntEnum
from core.entity import Entity
from dataclasses import dataclass, field
from time import time

class OtpStatus(IntEnum):
    PENDING = 0
    SUCCESS = 2

def get_expiration_time():
    return int(time()) + 60*10

@dataclass
class OtpInfo(Entity):
    phone: str = None
    otp: int = None
    status: int = field(default=OtpStatus.PENDING)
    expiration_time: int = field(default_factory=get_expiration_time)
