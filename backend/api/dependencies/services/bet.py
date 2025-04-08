from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import BetModel
from core.models.db_helper import db_helper
from core.models.event import OutComeModel
from core.repository.bet import SQLAlchemyBetRepository, AbstractBetRepository
from core.repository.event import SQLAlchemyOutComeRepository, AbstractEventRepository, AbstractOutComeRepository
from core.repository.user import AbstractUserRepository
from core.service.bet import BetService
from core.service.user import UserPermissionsService
from .user import get_user_permissions_service, get_sqlalchemy_user_repository
from .event import sqlalchemy_event_repo


async def sqlalchemy_bet_repo(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SQLAlchemyBetRepository:
    return SQLAlchemyBetRepository(session=session, model=BetModel)


async def sqlalchemy_outcome_repo(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SQLAlchemyOutComeRepository:
    return SQLAlchemyOutComeRepository(session=session, model=OutComeModel)


async def bet_service(
        repo: Annotated[AbstractBetRepository, Depends(sqlalchemy_bet_repo)],
        permissions_service: Annotated[UserPermissionsService, Depends(get_user_permissions_service)],
        user_repo: Annotated[AbstractUserRepository, Depends(get_sqlalchemy_user_repository)],
        event_repo: Annotated[AbstractEventRepository, Depends(sqlalchemy_event_repo)],
        outcome_repo: Annotated[AbstractOutComeRepository, Depends(sqlalchemy_outcome_repo)],
) -> BetService:
    return BetService(
        repo=repo,
        permissions_service=permissions_service,
        user_repository=user_repo,
        event_repository=event_repo,
        outcome_repository=outcome_repo,
    )
