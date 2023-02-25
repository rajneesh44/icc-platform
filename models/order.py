from dataclasses import dataclass, field
from core.entity import Entity
from enum import IntEnum


class OrderStatus(IntEnum):
    PENDING = 0
    SUCCESS = 1
    FAILED = 2



@dataclass
class Order(Entity):
    cart_id: str = None
    user_id: str = None
    status: int = OrderStatus.PENDING
    payment_id: str = None
    payment_status: str = None
    meta: dict = field(default_factory=dict)
    price: float = None
    discount: float = None
    final_price: float = None
