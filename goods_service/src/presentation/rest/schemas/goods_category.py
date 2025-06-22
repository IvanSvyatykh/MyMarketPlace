import uuid

from pydantic import BaseModel, Field


class AddGoodsCategoryRequest(BaseModel):
    category_name: str


class AddGoodsCategoryResponse(BaseModel):
    id: uuid.UUID
    category_name: str
