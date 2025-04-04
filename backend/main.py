from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.requests import Request

from api import router
from core.config import settings
from core.exceptions.user_exc import UserPermissionError
from core.models.db_helper import db_helper


# Lifespan приложения для освобождения пула соединений к базе данных.
@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    yield
    db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(router=router)


@app.exception_handler(UserPermissionError)
async def user_permission_handler(request: Request, exc: UserPermissionError):
    # Обработчик для исключения UserPermissionError
    raise HTTPException(status_code=403, detail="Insufficient access rights")


# Входная точка
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
