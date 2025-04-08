from abc import ABC, abstractmethod
from typing import Sequence

from sqlalchemy import select

from core.models import BetModel
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractReadRepository, SQLAlchemyAbstractWriteRepository


class AbstractBetRepository[Model](
    AbstractReadRepository[Model],
    AbstractWriteRepository[Model],
    ABC,
):
    # Специфичные методы для работы с BetModel
    @abstractmethod
    async def user_bets(self, user_id: int) -> Sequence[Model]:
        raise NotImplementedError()


class SQLAlchemyBetRepository(
    SQLAlchemyAbstractReadRepository[BetModel],
    SQLAlchemyAbstractWriteRepository[BetModel],
    AbstractBetRepository[BetModel],
):
    async def user_bets(self, user_id: int) -> Sequence[BetModel]:
        stmt = (
            select(BetModel)
            .where(BetModel.user_id == user_id)
        )
        result = await self._session.execute(stmt)
        return result.scalars().all()
