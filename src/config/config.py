from functools import lru_cache
from dotenv import load_dotenv

from domain.config import AppConfig, DatabaseConfig, ServerConfig


@lru_cache
def get_app_config() -> AppConfig:
    """
    Return application config
    """
    load_dotenv()
    server_config = ServerConfig()
    database_config = DatabaseConfig()

    return AppConfig(database=database_config, server=server_config)
