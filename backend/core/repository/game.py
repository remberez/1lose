from abc import ABC

from sqlalchemy import select, delete, update
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

    async def get(self, game_id: int) -> SQLAlchemyGameModel | None:
        res = await self._session.get(SQLAlchemyGameModel, game_id)
        return res

    async def delete(self, model_id: int) -> None:
        stmt = delete(SQLAlchemyGameModel).where(SQLAlchemyGameModel.id == model_id)
        await self._session.execute(stmt)
        await self._session.commit()

    async def update(self, model_id: int, **data) -> SQLAlchemyGameModel | None:
        stmt = update(SQLAlchemyGameModel).where(SQLAlchemyGameModel.id == model_id).values(**data)
        await self._session.execute(stmt)

        updated_game = await self._session.get(SQLAlchemyGameModel, model_id)
        await self._session.commit()
        await self._session.refresh(updated_game)
        return updated_game

    async def create(self, **model_data) -> SQLAlchemyGameModel:
        game = SQLAlchemyGameModel(**model_data)
        self._session.add(game)
        await self._session.commit()
        await self._session.refresh(game)
        return game
