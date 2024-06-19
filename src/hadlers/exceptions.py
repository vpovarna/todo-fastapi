from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR


def add_internal_server_error_handler(app: FastAPI) -> None:
    """
    Handle http exceptions.
    """

    @app.exception_handler(Exception)
    async def _exception_handler(_: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "status": HTTP_500_INTERNAL_SERVER_ERROR,
                "type": "HTTPException",
                "message": "Internal Server Error",
            },
        )


def add_exceptions_handlers(app: FastAPI) -> None:
    """
    Base exception handler
    """
    add_internal_server_error_handler(app)