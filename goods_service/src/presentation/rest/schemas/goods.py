import uuid

from pydantic import BaseModel, Field


class AddGoodRequest(BaseModel):
    name: str
    category_name: str
    price: float = Field(default=0.0, ge=0.0)
    amount: int = Field(default=0, ge=0)


class GetGoodsRequest(BaseModel):
    offset: int = Field(default=0, ge=0)
    limit: int = Field(default=10, ge=0)


class GetGoodsResponse(BaseModel):
    id: uuid.UUID
    name: str
    category_name: str
    photo_url: str
    price: float = Field(default=0.0, ge=0.0)
    amount: int = Field(default=0, ge=0)
