from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunSettings(BaseModel):
    port: int = 8000
    host: str = "localhost"
    reload: bool = True


class APISettings(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    run: RunSettings = RunSettings()
    api: APISettings = APISettings()


settings = Settings()
