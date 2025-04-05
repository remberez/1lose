import typing
from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from core.repository.match import SQLAlchemyMatchRepository
from .user import get_user_permissions_service
from core.service.match import MatchService

if typing.TYPE_CHECKING:
    from core.service.user import UserPermissionsService


async def sqlalchemy_match_repo(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SQLAlchemyMatchRepository:
    return SQLAlchemyMatchRepository(session=session)


async def match_service(
        match_repo: Annotated[SQLAlchemyMatchRepository, Depends(sqlalchemy_match_repo)],
        permissions_service: Annotated["UserPermissionsService", Depends(get_user_permissions_service)],
) -> MatchService:
    return MatchService(
        repository=match_repo,
        permissions_service=permissions_service
    )
