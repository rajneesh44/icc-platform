from core.entity import Entity
from pydantic.dataclasses import Field
import uuid

class Product(Entity):
    name: str = None
    description: str = None
    uuid: str = Field(default=str(uuid.uuid4()))
    images: list[str] = []
    display_image: str = None
    quantity: int = 0
    price: int = 0
    discount: int = 0
    ratings: int = 0
    sizes: list[str] = Field(default=["S", "M", "L", "XXL"])

