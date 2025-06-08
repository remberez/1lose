from abc import ABC

from core.models import EventModel
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractWriteRepository, SQLAlchemyAbstractReadRepository


class AbstractEventTypeRepository[ModelT](
    AbstractReadRepository,
    AbstractWriteRepository,
    ABC
):
    pass


class SQLAlchemyEventTypeRepository(
    AbstractEventTypeRepository[EventModel],
    SQLAlchemyAbstractWriteRepository[EventModel],
    SQLAlchemyAbstractReadRepository[EventModel],
):
    pass
