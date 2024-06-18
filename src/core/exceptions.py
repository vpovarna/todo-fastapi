class BaseInternalException(Exception):
    """
    Base error class for inherit all internal errors.
    """

    def __init__(self, message: str, status_code: int) -> None:
        self.message = message
        self.status_code = status_code


class UserAlreadyExistException(BaseInternalException):
    """
    Exception raised when user try to login with invalid username.
    """
