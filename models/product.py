from core.entity import Entity
import uuid
from dataclasses import dataclass, field
class Product(Entity):
    name: str = None
    description: str = None
    uuid: str = field(default=str(uuid.uuid4()))
    images: list[str] = []
    display_image: str = None
    quantity: int = 0
    price: int = 0
    discount: int = 0
    ratings: int = 0
    published: bool = False
    sizes: list[str] = field(default=["S", "M", "L", "XXL"])

