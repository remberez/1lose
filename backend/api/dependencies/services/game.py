from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.services.user import get_sqlalchemy_user_repository
from core.models.db_helper import db_helper
from core.repository.game import SQLAlchemyGameRepository, AbstractGameRepository
from core.repository.user import AbstractUserRepository
from core.service.game import GameService
from core.service.user import UserPermissionsService
from .user import get_user_permissions_service
from core.models.game import GameModel


async def get_sqlalchemy_game_repository(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SQLAlchemyGameRepository:
    return SQLAlchemyGameRepository(session=session, model=GameModel)


async def get_game_service(
    repository: Annotated[
        AbstractGameRepository, Depends(get_sqlalchemy_game_repository)
    ],
    user_repository: Annotated[
        AbstractUserRepository, Depends(get_sqlalchemy_user_repository)
    ],
    permissions_service: Annotated[
        UserPermissionsService,
        Depends(get_user_permissions_service),
    ],
) -> GameService:
    return GameService(
        repository=repository,
        user_repository=user_repository,
        permissions_service=permissions_service,
    )
