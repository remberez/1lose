from abc import ABC

from core.models import MapModel
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractWriteRepository, SQLAlchemyAbstractReadRepository


class AbstractMapRepository[MatchT](
    AbstractReadRepository[MatchT],
    AbstractWriteRepository[MatchT],
    ABC,
):
    # Специфичные методы для работы с MapModel
    ...


class SQLAlchemyMapRepository(
    AbstractMapRepository[MapModel],
    SQLAlchemyAbstractReadRepository[MapModel],
    SQLAlchemyAbstractWriteRepository[MapModel],
):
    ...
