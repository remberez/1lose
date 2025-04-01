from fastapi.params import Depends
from fastapi_users.authentication.strategy import AccessTokenDatabase, DatabaseStrategy
from typing_extensions import Annotated

from .access_token import get_access_token_db
from core.config import settings
from core.models import AccessTokenModel


def get_database_strategy(
    access_token_db: Annotated[
        AccessTokenDatabase[AccessTokenModel],
        Depends(get_access_token_db),
    ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_token_db,
        lifetime_seconds=settings.auth.lifetime_seconds,
    )
