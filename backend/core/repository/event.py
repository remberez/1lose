from abc import ABC
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from core.models import EventModel, MatchModel, MapModel
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractReadRepository, SQLAlchemyAbstractWriteRepository


class AbstractEventRepository[Model](
    AbstractReadRepository[Model],
    AbstractWriteRepository[Model],
    ABC,
):
    # Специфичные методы для работы с EventModel
    ...


class SQLAlchemyEventRepository(
    AbstractEventRepository[EventModel],
    SQLAlchemyAbstractReadRepository[EventModel],
    SQLAlchemyAbstractWriteRepository[EventModel],
):
    async def list(self, *args, **kwargs) -> Sequence[EventModel]:
        stmt = (
            select(EventModel)
            .where(**kwargs)
            .options(
                joinedload(EventModel.match)
                    .joinedload(MatchModel.tournament)
                    .joinedload(MatchModel.first_team)
                    .joinedload(MatchModel.second_team),
                joinedload(EventModel.map)
                    .joinedload(MapModel.match),
                joinedload(EventModel.first_outcome),
                joinedload(EventModel.second_outcome),
            )
        )
        result = await self._session.execute(stmt)
        return result.scalars().all()
