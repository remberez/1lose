from abc import ABC
from typing_extensions import TypeVar

from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractWriteRepository, SQLAlchemyAbstractReadRepository
from core.models.match import MatchModel

MatchT = TypeVar("MatchT")


class AbstractMatchRepository(
    AbstractReadRepository[MatchT],
    AbstractWriteRepository[MatchT],
    ABC,
):
    # Специфичные методы для работы с MatchModel
    ...


class SQLAlchemyMatchRepository(
    SQLAlchemyAbstractWriteRepository[MatchModel],
    SQLAlchemyAbstractReadRepository[MatchModel],
    AbstractMatchRepository,
):
    ...
