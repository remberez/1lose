from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from core.repository.user import AbstractUserRepository, UserSQLAlchemyRepository
from core.service.user import UserService, UserPermissionsService
from core.models.user import UserModel


async def get_sqlalchemy_user_repository(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> UserSQLAlchemyRepository:
    return UserSQLAlchemyRepository(session=session, model=UserModel)


async def get_user_permissions_service(
    repository: Annotated[
        AbstractUserRepository, Depends(get_sqlalchemy_user_repository)
    ],
) -> UserPermissionsService:
    return UserPermissionsService(user_repository=repository)


async def get_user_service(
    repository: Annotated[
        AbstractUserRepository, Depends(get_sqlalchemy_user_repository)
    ],
    permissions_service: Annotated[
        UserPermissionsService, Depends(get_user_permissions_service),
    ]
) -> UserService:
    return UserService(repository=repository, permissions_service=permissions_service)
