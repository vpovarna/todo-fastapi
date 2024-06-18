from fastapi import Depends

from core.exceptions import UserAlreadyExistException
from core.logger import logger
from starlette.status import HTTP_401_UNAUTHORIZED
from db.repository.users import UsersRepository, get_users_repository
from core.models.users import User, UserCreateDTO


class UserService:
    def __init__(self, user_repo: UsersRepository = Depends(get_users_repository)) -> None:
        self.user_repo = user_repo

    def register_user(self, user_create: UserCreateDTO) -> User:
        """
        Register user in application
        """

        logger.info(f"Try to find user: {user_create.username}")
        db_user = self.user_repo.get_by_username(username=user_create.username)
        if db_user:
            raise UserAlreadyExistException(
                message=f"User with username: `{user_create.username}` already exists",
                status_code=HTTP_401_UNAUTHORIZED
            )
        user = self.user_repo.create(obj_create=user_create)
        logger.info(f"User: {user_create.username} created")
        return user
