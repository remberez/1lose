from abc import ABC
from typing import Sequence

from sqlalchemy import select, update, delete
from typing_extensions import TypeVar

from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractRepository
from core.models.match import MatchModel

MatchT = TypeVar("MatchT")


class AbstractMatchRepository(
    AbstractReadRepository[MatchT],
    AbstractWriteRepository[MatchT],
    ABC,
):
    # Специфичные методы для работы с MatchModel
    ...


class SQLAlchemyTournamentRepository(
    SQLAlchemyAbstractRepository[MatchModel],
    AbstractMatchRepository,
):
    async def list(self, *args, **kwargs) -> Sequence[MatchModel]:
        stmt = select(MatchModel)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def create(self, **data) -> MatchModel:
        match = MatchModel(**data)
        self._session.add(match)
        await self._session.commit()
        await self._session.refresh(match)
        return match

    async def update(self, model_id: int, **data) -> MatchModel:
        stmt = (
            update(MatchModel)
            .where(MatchModel.id == model_id)
            .values(**data)
        )
        await self._session.execute(stmt)
        await self._session.commit()

        return await self.get(model_id)

    async def get(self, model_id: int) -> MatchModel | None:
        return await self._session.get(MatchModel, model_id)

    async def delete(self, model_id: int) -> None:
        stmt = (
            delete(MatchModel)
            .where(MatchModel.id == model_id)
        )
        await self._session.execute(stmt)
        await self._session.commit()
