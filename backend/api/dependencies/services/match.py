import typing
from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from core.repository.match import SQLAlchemyMatchRepository
from core.service.match import MatchService
from .tournament import get_sqlalchemy_tournament_repository
from .user import get_user_permissions_service

if typing.TYPE_CHECKING:
    from core.service.user import UserPermissionsService
    from core.repository.tournament import SQLAlchemyTournamentRepository

async def sqlalchemy_match_repo(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SQLAlchemyMatchRepository:
    return SQLAlchemyMatchRepository(session=session)


async def match_service(
        match_repo: Annotated[SQLAlchemyMatchRepository, Depends(sqlalchemy_match_repo)],
        permissions_service: Annotated["UserPermissionsService", Depends(get_user_permissions_service)],
        tournament_repo: Annotated["SQLAlchemyTournamentRepository", Depends(get_sqlalchemy_tournament_repository)]
) -> MatchService:
    return MatchService(
        repository=match_repo,
        permissions_service=permissions_service,
        tournament_repository=tournament_repo,
    )
