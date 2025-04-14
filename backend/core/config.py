from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunSettings(BaseModel):
    port: int = 8000
    host: str = "localhost"
    reload: bool = True


class APISettings(BaseModel):
    prefix: str = "/api"
    auth: str = "/auth"
    games: str = "/games"
    teams: str = "/ea-teams"
    tournament: str = "/tournaments"
    match: str = "/matches"
    map: str = "/maps"
    event: str = "/events"
    bet: str = "/bets"
    business: str = "/business-settings"

    @property
    def token_url(self) -> str:
        parts = (self.prefix, self.auth, "/login")
        path = "".join(parts)
        return path.removeprefix("/")


class DataBaseSettings(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class AuthSettings(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP__",
        env_file=".env",
    )

    run: RunSettings = RunSettings()
    api: APISettings = APISettings()
    database: DataBaseSettings
    auth: AuthSettings


settings = Settings()
