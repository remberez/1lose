from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunSettings(BaseModel):
    port: int = 8000
    host: str = "localhost"
    reload: bool = True


class APISettings(BaseModel):
    prefix: str = "/api"


class DataBaseSettings(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP__",
        env_file=".env"
    )

    run: RunSettings = RunSettings()
    api: APISettings = APISettings()
    database: DataBaseSettings


settings = Settings()
