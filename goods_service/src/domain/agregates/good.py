import uuid
from dataclasses import dataclass


@dataclass
class Good:
    id: uuid.UUID | None
    category_name: str
    name: str
    price: float
    amount: int

    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4()
