from abc import ABC

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from core.models.event import EventTypeModel
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractWriteRepository, SQLAlchemyAbstractReadRepository


class AbstractEventTypeRepository[ModelT](
    AbstractReadRepository,
    AbstractWriteRepository,
    ABC
):
    pass


class SQLAlchemyEventTypeRepository(
    AbstractEventTypeRepository[EventTypeModel],
    SQLAlchemyAbstractWriteRepository[EventTypeModel],
    SQLAlchemyAbstractReadRepository[EventTypeModel],
):
    async def get(self, code: int) -> EventTypeModel:
        stmt = (
            select(EventTypeModel)
            .where(EventTypeModel.code == code)
            .options(
                joinedload(EventTypeModel.game)
            )
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()
