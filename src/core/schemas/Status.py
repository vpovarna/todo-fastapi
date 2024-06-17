from pydantic import BaseModel


class Status(BaseModel):
    success: bool
    version: str
    message: str
