from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.v1.router import router as api_router
from db.session import Base, session
from hadlers.exceptions import add_exceptions_handlers


def create_app() -> FastAPI:
    """
    Application factory method, used to crate FAST API application
    :return: FastAPI
    """

    # TODO: Add application settings

    application = FastAPI()

    # Database initialization
    Base.metadata.create_all(session)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix="/api")
    add_exceptions_handlers(app=application)

    return application


app = create_app()
