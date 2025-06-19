import uuid

from pydantic import BaseModel


class GoodsRequest(BaseModel):
    offset: int
    limit: int


class GoodsResponse(BaseModel):
    id: uuid.UUID
    name: str
    category_name: str
    photo_url: str
    price: float
    amount: int
