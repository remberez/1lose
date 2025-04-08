from abc import ABC
from decimal import Decimal

from black.nodes import TypeVar
from sqlalchemy import select, update

from core.repository.abc import AbstractReadRepository
from core.models.user import UserModel
from .sqlalchemy import (
    SQLAlchemyAbstractReadRepository,
    SQLAlchemyAbstractWriteRepository,
)

UserModelT = TypeVar("UserModelT")


class AbstractUserRepository(
    AbstractReadRepository[UserModelT],
    ABC,
):
    # Специфичные методы для работы с пользователями.
    async def get_user_balance(self, user_id: int) -> Decimal:
        raise NotImplementedError()

    async def update_user_balance(self, user_id: int, value: Decimal) -> Decimal:
        raise NotImplementedError()


class UserSQLAlchemyRepository(
    SQLAlchemyAbstractReadRepository[UserModel],
    SQLAlchemyAbstractWriteRepository[UserModel],
    AbstractUserRepository,
):
    async def get_user_balance(self, user_id: int) -> Decimal:
        stmt = (
            select(UserModel.balance)
            .where(UserModel.id == user_id)
        )
        result = await self._session.execute(stmt)
        return result.scalar_one()

    async def update_user_balance(self, user_id: int, value: Decimal) -> Decimal:
        user = await self.get(user_id)
        user.balance += value
        await self._session.commit()
        return user.balance

