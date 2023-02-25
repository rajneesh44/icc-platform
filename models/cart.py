from dataclasses import dataclass, field, asdict
from core.entity import Entity
from models.product import Product


@dataclass
class Cart(Entity):
    products: list[Product] = field(default_factory=list)
    user_id: str = None
    price: int = field(default=0)
