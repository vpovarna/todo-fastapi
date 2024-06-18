from typing import Optional

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    fullname: str


class UserCreateDTO(User):
    password: str


class UserUpdateDTO(User):
    password: Optional[str] = None
