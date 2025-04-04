from abc import ABC
from typing import Sequence

from sqlalchemy import select, update, delete
from sqlalchemy.orm import joinedload
from typing_extensions import TypeVar

from .abc import AbstractReadRepository, AbstractWriteRepository
from .sqlalchemy import SQLAlchemyAbstractRepository
from core.models.team import EATeamModel

EATeamModelT = TypeVar("EATeamModelT")


class AbstractEATeamRepository(
    AbstractReadRepository[EATeamModelT],
    AbstractWriteRepository,
    ABC,
):
    # Специфичные методы для работы с EATeamModel
    ...


class SQLAlchemyEATeamRepository(
    SQLAlchemyAbstractRepository[EATeamModel],
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

    async def create(self, **data) -> EATeamModel | None:
        team = EATeamModel(**data)
        self._session.add(team)
        await self._session.commit()
        await self._session.refresh(team)
        return team

    async def update(self, team_id: int, **data) -> EATeamModel | None:
        stmt = update(EATeamModel).where(EATeamModel.id == team_id).values(**data)
        await self._session.execute(stmt)

        updated_team = await self.get(team_id)
        await self._session.commit()
        await self._session.refresh(updated_team)

        return updated_team

    async def delete(self, team_id: int) -> None:
        stmt = delete(EATeamModel).where(EATeamModel.id == team_id)
        await self._session.execute(stmt)
        await self._session.commit()
