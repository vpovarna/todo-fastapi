from pydantic_settings import BaseSettings


class BaseAppSettings(BaseSettings):
    """
    Base application setting class
    """

    class Config:
        env_file = ".env"
