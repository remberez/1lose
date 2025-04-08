from abc import ABC

from core.models import BetModel
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractReadRepository, SQLAlchemyAbstractWriteRepository


class AbstractBetRepository[Model](
    AbstractReadRepository[Model],
    AbstractWriteRepository[Model],
    ABC,
):
    # Специфичные методы для работы с BetModel
    ...


class SQLAlchemyBetRepository(
    SQLAlchemyAbstractReadRepository[BetModel],
    SQLAlchemyAbstractWriteRepository[BetModel],
    AbstractBetRepository[BetModel],
):
    ...
