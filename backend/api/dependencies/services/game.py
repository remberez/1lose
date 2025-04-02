from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from core.repository.game import SQLAlchemyGameRepository, GameRepository
from core.service.game import GameService


async def get_sqlalchemy_game_repository(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SQLAlchemyGameRepository:
    return SQLAlchemyGameRepository(session=session)


async def get_game_service(
    repository: Annotated[GameRepository, Depends(get_sqlalchemy_game_repository)],
) -> GameService:
    return GameService(repository=repository)
