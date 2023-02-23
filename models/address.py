from dataclasses import dataclass, field
from core.entity import Entity

@dataclass
class Address(Entity):
    user_id: str = None
    default: bool = field(default=False)
    building_number: str = None
    colony: str = None
    area: str = None
    landmark: str = None
    city: str = None
    state: str = None
    country: str = None
    pincode: str = None
