from abc import ABC

from typing_extensions import TypeVar

from core.models.game import GameModel as SQLAlchemyGameModel
from .abc import AbstractRepository
from .sqlalchemy import SQLAlchemyAbstractRepository

GameModel = TypeVar("GameModel")


class GameRepository(AbstractRepository[GameModel], ABC):
    # Специфичные методы для работы с моделью Game.
    ...


class SQLAlchemyGameRepository(
    SQLAlchemyAbstractRepository[SQLAlchemyGameModel],
    GameRepository,
):
    async def list(self, *args, **kwargs) -> list[SQLAlchemyGameModel]:
        raise NotImplementedError()

    async def get(self, **kwargs) -> SQLAlchemyGameModel:
        raise NotImplementedError()

    async def delete(self, model_id: int) -> None:
        raise NotImplementedError()

    async def update(self, model_id: int, **data) -> SQLAlchemyGameModel:
        raise NotImplementedError()

    async def create(self, **model_data) -> SQLAlchemyGameModel:
        game = SQLAlchemyGameModel(**model_data)
        self._session.add(game)
        await self._session.commit()
        await self._session.refresh(game)
        return game
