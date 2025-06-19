import uuid
from dataclasses import dataclass


@dataclass
class Good:
    id: uuid.UUID
    category_name: str
    name: str
    photo_url: str
    price: float
    amount: int
