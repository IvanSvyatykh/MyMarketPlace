from pydantic import BaseModel, EmailStr


class AddUserRequestDTO(BaseModel):
    email: EmailStr
    name: str
    password: str
