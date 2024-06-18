from sqlalchemy import Column, Integer, String, Boolean

from core.security import get_password_hash
from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String)
    full_name = Column(String)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, default=False)

    def __init__(self, username: str, email: str, full_name: str, password: str) -> None:
        self.username = username
        self.email = email
        self.full_name = full_name
        self.hashed_password = get_password_hash(password=password)
