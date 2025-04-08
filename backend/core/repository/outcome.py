from abc import ABC

from core.models.event import OutComeModel
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractWriteRepository, SQLAlchemyAbstractReadRepository


class AbstractOutComeRepository[Model](
    AbstractReadRepository[Model],
    AbstractWriteRepository[Model],
    ABC,
):
    # Специфичные методы для работы с OutComeModel
    ...


class SQLAlchemyOutComeRepository(
    AbstractOutComeRepository[OutComeModel],
    SQLAlchemyAbstractWriteRepository[OutComeModel],
    SQLAlchemyAbstractReadRepository[OutComeModel],
):
    ...
