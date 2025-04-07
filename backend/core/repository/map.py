from abc import ABC, abstractmethod

from sqlalchemy import select

from core.models import MapModel
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractWriteRepository, SQLAlchemyAbstractReadRepository


class AbstractMapRepository[MatchT](
    AbstractReadRepository[MatchT],
    AbstractWriteRepository[MatchT],
    ABC,
):
    # Специфичные методы для работы с MapModel
    @abstractmethod
    async def get_match_id(self, map_id: int) -> int:
        raise NotImplementedError()


class SQLAlchemyMapRepository(
    AbstractMapRepository[MapModel],
    SQLAlchemyAbstractReadRepository[MapModel],
    SQLAlchemyAbstractWriteRepository[MapModel],
):
    async def get_match_id(self, map_id: int) -> int:
        stmt = select(MapModel.match_id)
        result = await self._session.execute(stmt)
        return result.scalar()
