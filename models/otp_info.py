from enum import IntEnum
from core.entity import Entity
from pydantic.dataclasses import Field
from time import time


class OtpStatus(IntEnum):
    PENDING = 0
    SUCCESS = 2

def get_expiration_time():
    return int(time()) + 60*10

class OtpInfo(Entity):
    phone: str = None
    otp: int = None
    status: int = Field(default=OtpStatus.PENDING)
    expiration_time: int = Field(default_factory=get_expiration_time)
