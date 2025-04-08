from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated

from core.models import EventModel
from core.models.db_helper import db_helper
from core.models.event import OutComeModel
from core.repository.event import SQLAlchemyEventRepository, AbstractEventRepository
from core.repository.map import AbstractMapRepository
from core.repository.outcome import SQLAlchemyOutComeRepository, AbstractOutComeRepository
from core.service.user import UserPermissionsService
from .user import get_user_permissions_service
from core.service.event import EventService
from .map import sqlalchemy_map_repo


async def sqlalchemy_event_repo(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SQLAlchemyEventRepository:
    return SQLAlchemyEventRepository(session=session, model=EventModel)


async def sqlalchemy_outcome_repo(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SQLAlchemyOutComeRepository:
    return SQLAlchemyOutComeRepository(session=session, model=OutComeModel)


async def event_service(
        repo: Annotated[AbstractEventRepository, Depends(sqlalchemy_event_repo)],
        permissions_service: Annotated[UserPermissionsService, Depends(get_user_permissions_service)],
        map_repo: Annotated[AbstractMapRepository, Depends(sqlalchemy_map_repo)],
        outcome_repo: Annotated[AbstractOutComeRepository, Depends(sqlalchemy_outcome_repo)]
) -> EventService:
    return EventService(
        repository=repo,
        permissions_service=permissions_service,
        map_repo=map_repo,
        outcome_repo=outcome_repo,
    )
