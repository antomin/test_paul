import uvicorn
from fastapi import FastAPI

from app.api import router as main_router
from config import settings


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(main_router)

    return app


if __name__ == "__main__":
    uvicorn.run(
        "main:create_app",
        factory=True,
        host=settings.APP_HOST,
        port=settings.APP_PORT,
    )
