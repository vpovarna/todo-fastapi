from fastapi import APIRouter

from domain.status import Status

router = APIRouter()


@router.get("", response_model=Status)
def status() -> Status:
    """
    Health check api
    :return: Status
    """
    return Status(
        status=True,
        version="1.0.0",
        message="FastAPI ToDo Application"
    )
