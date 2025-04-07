from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import MapModel
from core.models.db_helper import db_helper
from core.repository.map import SQLAlchemyMapRepository
from core.service.map import MapService
from core.service.user import UserPermissionsService
from .user import get_user_permissions_service


async def sqlalchemy_map_repo(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SQLAlchemyMapRepository:
    return SQLAlchemyMapRepository(session=session, model=MapModel)


async def map_service(
        repo: Annotated[SQLAlchemyMapRepository, Depends(sqlalchemy_map_repo)],
        permissions_service: Annotated[UserPermissionsService, Depends(get_user_permissions_service)],
) -> MapService:
    return MapService(
        repository=repo,
        permissions_service=permissions_service,
    )
