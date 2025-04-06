from abc import ABC

from typing_extensions import TypeVar

from core.models.game import GameModel as SQLAlchemyGameModel
from .abc import AbstractReadRepository, AbstractWriteRepository
from .sqlalchemy import (
    SQLAlchemyAbstractWriteRepository,
    SQLAlchemyAbstractReadRepository,
)

GameModel = TypeVar("GameModel")


class AbstractGameRepository(
    AbstractReadRepository[GameModel], AbstractWriteRepository[GameModel], ABC
):
    # Специфичные методы для работы с моделью Game.
    ...


class SQLAlchemyGameRepository(
    SQLAlchemyAbstractWriteRepository[SQLAlchemyGameModel],
    SQLAlchemyAbstractReadRepository[SQLAlchemyGameModel],
    AbstractGameRepository,
): ...
