from typing_extensions import TypeVar

from .sqlalchemy import SQLAlchemyAbstractRepository
from abc import ABC
from .abc import AbstractRepository
from core.models.game import GameModel as SQLAlchemyGameModel


GameModel = TypeVar("GameModel")


class GameRepository(AbstractRepository[GameModel], ABC):
    async def list(self, *args, **kwargs) -> list[GameModel]:
        raise NotImplementedError()

    async def get(self, **kwargs) -> GameModel:
        raise NotImplementedError()

    async def delete(self, model_id: int) -> None:
        raise NotImplementedError()

    async def update(self, model_id: int, **data) -> GameModel:
        raise NotImplementedError()

    async def create(self, **model_data) -> GameModel:
        raise NotImplementedError()


class SQLAlchemyGameRepository(
    SQLAlchemyAbstractRepository[SQLAlchemyGameModel], GameRepository
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
