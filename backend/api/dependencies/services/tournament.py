from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from core.repository.tournament import SQLAlchemyTournamentRepository
from core.service.tournament import TournamentService
from core.service.user import UserPermissionsService
from .user import get_user_permissions_service


async def get_sqlalchemy_tournament_repository(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SQLAlchemyTournamentRepository:
    return SQLAlchemyTournamentRepository(session=session)


async def get_tournament_service(
        repository: Annotated[SQLAlchemyTournamentRepository, Depends(get_sqlalchemy_tournament_repository)],
        permission_service: Annotated[UserPermissionsService, Depends(get_user_permissions_service)],
) -> TournamentService:
    return TournamentService(
        repository=repository,
        permissions_service=permission_service
    )
