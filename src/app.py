from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.config import get_app_settings
from src.api.v1.router import router as api_router


def create_app():
    """
    FastAPI application factory method.
    """

    settings = get_app_settings()

    application = FastAPI()

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix="/api/v1")

    return application


app = create_app()
