from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import router
import uvicorn
from core.config import settings
from core.models.db_helper import db_helper


# Lifespan приложения для освобождения пула соеденений к базе данных.
@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    yield
    db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(router=router)

# Входная точка
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
