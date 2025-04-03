from abc import ABC

from sqlalchemy import select
from typing_extensions import TypeVar, Sequence

from core.models.game import GameModel as SQLAlchemyGameModel
from .abc import AbstractReadRepository, AbstractWriteRepository
from .sqlalchemy import SQLAlchemyAbstractRepository

GameModel = TypeVar("GameModel")


class AbstractGameRepository(
    AbstractReadRepository[GameModel],
    AbstractWriteRepository[GameModel],
    ABC
):
    # Специфичные методы для работы с моделью Game.
    ...


class SQLAlchemyGameRepository(
    SQLAlchemyAbstractRepository[SQLAlchemyGameModel],
    AbstractGameRepository,
):
    async def list(self, *args, **kwargs) -> Sequence[SQLAlchemyGameModel]:
        stmt = select(SQLAlchemyGameModel)
        result = await self._session.execute(stmt)
        return result.scalars().all()

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
