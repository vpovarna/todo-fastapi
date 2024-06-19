from fastapi import APIRouter

from api.v1.routes import status

router = APIRouter()

router.include_router(router=status.router, tags=["Status"], prefix="/status")
