from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from core.repository.team import SQLAlchemyEATeamRepository, AbstractEATeamRepository
from core.repository.user import AbstractUserRepository
from core.service.team import EATeamService
from .user import get_sqlalchemy_user_repository


async def get_sqlalchemy_ea_team_repository(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> SQLAlchemyEATeamRepository:
    return SQLAlchemyEATeamRepository(session=session)


async def get_ea_team_service(
        repository: Annotated[AbstractEATeamRepository, Depends(get_sqlalchemy_ea_team_repository)],
        user_repository: Annotated[AbstractUserRepository, Depends(get_sqlalchemy_user_repository)],
) -> EATeamService:
    return EATeamService(repository=repository, user_repository=user_repository)
