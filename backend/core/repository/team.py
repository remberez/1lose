from abc import ABC, abstractmethod
from typing import Sequence

from sqlalchemy import select, delete, exists
from sqlalchemy.orm import joinedload
from typing_extensions import TypeVar

from .abc import AbstractReadRepository, AbstractWriteRepository
from .sqlalchemy import (
    SQLAlchemyAbstractReadRepository,
    SQLAlchemyAbstractWriteRepository,
)
from core.models.team import EATeamModel
from core.exceptions.common import NotFoundError

EATeamModelT = TypeVar("EATeamModelT")


class AbstractEATeamRepository(
    AbstractReadRepository[EATeamModelT],
    AbstractWriteRepository[EATeamModelT],
    ABC,
):
    @abstractmethod
    async def team_exists(self, team_id: int):
        raise NotImplementedError()


class SQLAlchemyEATeamRepository(
    SQLAlchemyAbstractReadRepository[EATeamModel],
    SQLAlchemyAbstractWriteRepository[EATeamModel],
    AbstractEATeamRepository,
):
    async def list(self) -> Sequence[EATeamModel]:
        stmt = select(EATeamModel).options(joinedload(EATeamModel.game))
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def get(self, team_id: int) -> EATeamModel | None:
        stmt = (
            select(EATeamModel)
            .where(EATeamModel.id == team_id)
            .options(joinedload(EATeamModel.game))
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, **data) -> EATeamModel:
        team = EATeamModel(**data)
        self._session.add(team)
        return team

    async def delete(self, team_id: int) -> None:
        stmt = delete(EATeamModel).where(EATeamModel.id == team_id)
        await self._session.execute(stmt)

    async def team_exists(self, team_id: int):
        # Вызывает NotFoundError, если команда не была найдена.
        stmt = select(exists().where(EATeamModel.id == team_id))
        if not bool(await self._session.scalar(stmt)):
            raise NotFoundError(f"Tournament {team_id} not found")
