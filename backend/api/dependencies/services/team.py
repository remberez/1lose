from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from core.repository.team import SQLAlchemyEATeamRepository, AbstractEATeamRepository
from core.repository.user import AbstractUserRepository
from core.service.team import EATeamService
from core.service.user import UserPermissionsService
from .user import get_sqlalchemy_user_repository, get_user_permissions_service
from core.models.team import EATeamModel


async def get_sqlalchemy_ea_team_repository(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SQLAlchemyEATeamRepository:
    return SQLAlchemyEATeamRepository(session=session, model=EATeamModel)


async def get_ea_team_service(
    repository: Annotated[
        AbstractEATeamRepository, Depends(get_sqlalchemy_ea_team_repository)
    ],
    user_repository: Annotated[
        AbstractUserRepository, Depends(get_sqlalchemy_user_repository)
    ],
    permissions_service: Annotated[
        UserPermissionsService, Depends(get_user_permissions_service)
    ],
) -> EATeamService:
    return EATeamService(
        repository=repository,
        user_repository=user_repository,
        permissions_service=permissions_service,
    )
