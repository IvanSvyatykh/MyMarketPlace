import uuid

from pydantic import BaseModel, Field

from goods_service.src.infrastructure.db.models.model import GoodsModel


class AddGoodRequest(BaseModel):
    name: str
    category_name: str
    price: float = Field(default=0.0, ge=0.0)
    amount: int = Field(default=0, ge=0)


class GetGoodsResponse(BaseModel):
    id: uuid.UUID
    name: str
    category_name: str
    price: float = Field(default=0.0, ge=0.0)
    amount: int = Field(default=0, ge=0)


class AddGoodPhotosRequest(BaseModel):
    good_id : uuid.UUID
    description :str