import uuid
from dataclasses import dataclass


@dataclass
class GoodCategory:
    id: uuid.UUID | None
    name: str

    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4()
