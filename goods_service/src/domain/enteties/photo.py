from pydantic import BaseModel, field_validator


class Photo(BaseModel):
    content: bytes
    filename: str
    content_type: str

    @field_validator("content")
    def validate_size(cls, v):
        if len(v) > 10 * 1024 * 1024:  # 10 MB
            raise ValueError("Photo size exceeds 10 MB")
        return v

    @field_validator("content_type")
    def validate_type(cls, v):
        if v not in {"image/jpeg", "image/png"}:
            raise ValueError("Invalid image type")
        return v
