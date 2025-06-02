from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

from api import router
from core.config import settings
from core.exceptions.common import NotFoundError, BusinessValidationError, AlreadyExistsError
from core.exceptions.match_exc import MatchInProgressException, MatchDateTimeException
from core.exceptions.user_exc import UserPermissionError
from core.models.db_helper import db_helper


# Lifespan приложения для освобождения пула соединений к базе данных.
@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    yield
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(router=router)
app.mount(settings.static_files.media_url, StaticFiles(directory=settings.static_files.media_path), name="media")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.allow_origins,
    allow_credentials=settings.cors.allow_credentials,
    allow_methods=settings.cors.allow_methods,
    allow_headers=settings.cors.allow_headers,
)

@app.exception_handler(UserPermissionError)
async def user_permission_handler(_request: Request, _exc: UserPermissionError):
    # Обработчик для исключения UserPermissionError
    raise HTTPException(status_code=403, detail="Insufficient access rights")


@app.exception_handler(NotFoundError)
async def not_found_handler(_request: Request, exc: NotFoundError):
    # Обработчик исключений для NotFoundError
    raise HTTPException(status_code=404, detail=exc.messages)


@app.exception_handler(MatchInProgressException)
async def match_progress_handler(_request: Request, exc: NotFoundError):
    raise HTTPException(status_code=400, detail=str(exc))


@app.exception_handler(MatchDateTimeException)
async def match_datetime_handler(_request, exc: MatchDateTimeException):
    raise HTTPException(status_code=400, detail=str(exc))


@app.exception_handler(BusinessValidationError)
async def business_validation_handler(_request: Request, exc: BusinessValidationError):
    raise HTTPException(status_code=400, detail=str(exc))


@app.exception_handler(AlreadyExistsError)
async def already_exists_handler(_request: Request, exc: AlreadyExistsError):
    raise HTTPException(status_code=409, detail=str(exc))


# Входная точка
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
