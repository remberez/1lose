from fastapi import FastAPI
from api import router
import uvicorn
from core.config import settings

app = FastAPI()
app.include_router(router=router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
