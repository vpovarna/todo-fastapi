from pydantic_settings import BaseSettings


class ServerConfig(BaseSettings):
    """
    Server config class
    """
    server_host: str
    server_port: int


class DatabaseConfig(BaseSettings):
    """
    Database configuration class
    """
    db_url: str
    db_password: str
    db_user: str
    db_thread_pool_size: int


class AppConfig(BaseSettings):
    """
    Application Config class
    """
    server: ServerConfig
    database: DatabaseConfig
