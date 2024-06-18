from typing import Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from core.config import get_app_settings
from db.repository.base import BaseRepository
from db.session import get_db
from core.models.users import UserCreateDTO, UserUpdateDTO, User

settings = get_app_settings()


class UsersRepository(BaseRepository[User, UserCreateDTO, UserUpdateDTO]):
    """
    Repository to manipulate users with the task
    """

    def get_by_username(self, username: str) -> Optional[User]:
        """
        Get user by `username` field
        """
        return self.db.query(User).filter(User.username == username).first()

    @staticmethod
    def is_active(user: User) -> bool:
        """
        Check if user is active
        """
        return not user.disabled


def get_users_repository(session: Session = Depends(get_db)) -> UsersRepository:
    return UsersRepository(db=session, model=User)
