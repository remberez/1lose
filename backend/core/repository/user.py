from abc import ABC
from decimal import Decimal

from black.nodes import TypeVar
from sqlalchemy import select, update, insert

from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.models.user import UserModel
from .sqlalchemy import (
    SQLAlchemyAbstractReadRepository,
    SQLAlchemyAbstractWriteRepository,
)

UserModelT = TypeVar("UserModelT")


class AbstractUserRepository(
    AbstractReadRepository[UserModelT],
    AbstractWriteRepository[UserModelT],
    ABC,
):
    # Специфичные методы для работы с пользователями.
    async def get_user_balance(self, user_id: int) -> Decimal:
        raise NotImplementedError()

    async def update_user_balance(self, user_id: int, value: Decimal) -> Decimal:
        raise NotImplementedError()

    async def get_user_by_email(self, email: str) -> UserModelT:
        raise NotImplementedError()

    async def create(self, email: str, hashed_password: str) -> UserModelT:
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
        return user.balance

    async def get_user_by_email(self, email: str) -> UserModel | None:
        stmt = (
            select(UserModel)
            .where(UserModel.email == email)
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, email: str, hashed_password: str) -> UserModel:
        model = UserModel(
            email=email,
            hashed_password=hashed_password,
        )
        self._session.add(model)
        await self._session.flush()
        return model
