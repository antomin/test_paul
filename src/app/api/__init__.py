from fastapi import APIRouter

from config import settings

from .task import router as tasks_router

router = APIRouter(prefix=settings.API_PATH_PREF)

router.include_router(tasks_router)
