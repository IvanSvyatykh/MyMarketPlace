import uuid

from pydantic import BaseModel, Field


class GetGoodsRequestDTO(BaseModel):
    offset: int = Field(default=0, ge=0)
    limit: int = Field(default=10, ge=0)


class GetGoodsResponseDTO(BaseModel):
    id: uuid.UUID
    category_name: str
    name: str
    price: float = Field(ge=0.0)
    amount: int = Field(ge=0)



class AddGoodRequestDTO(BaseModel):
    name: str
    category_name: str
    price: float = Field(default=0.0, ge=0.0)
    amount: int = Field(default=0, ge=0)