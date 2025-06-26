import uuid

from pydantic import BaseModel, Field


class AddGoodsCategoryRequest(BaseModel):
    category_name: str
