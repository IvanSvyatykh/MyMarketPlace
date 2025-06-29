from pydantic import BaseModel


class Photo(BaseModel):
    content: bytes
    filename: str
    content_type: str
