from core.entity import Entity
import uuid
from dataclasses import dataclass, field

def get_sizes():
    return ["S", "M", "L", "XXL"]


@dataclass
class Product(Entity):
    name: str = None
    description: str = None
    uuid: str = field(default=str(uuid.uuid4()))
    images: list[str] = field(default_factory=list)
    display_image: str = None
    quantity: int = 0
    price: int = 0
    discount: int = 0
    ratings: float = 0
    published: bool = False
    sizes: list[str] = field(default_factory=get_sizes)
    is_sku: bool = field(default=True)
    parent: str = None
    user_id: str = None

