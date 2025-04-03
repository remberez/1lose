from abc import ABC

from black.nodes import TypeVar
from core.repository.abc import AbstractReadRepository
from core.models.user import UserModel
from .sqlalchemy import SQLAlchemyAbstractRepository

UserModelT = TypeVar("UserModelT")


class AbstractUserRepository(
    AbstractReadRepository[UserModel],
    ABC,
):
    # Специфичные методы для работы с пользователями.
    ...


class UserSQLAlchemyRepository(SQLAlchemyAbstractRepository, AbstractUserRepository):
    # Реализация репозитория с помощью SQLAlchemy.
    async def get(self, user_id: int) -> UserModel | None:
        return await self._session.get(UserModel, user_id)

    async def list(self, *args, **kwargs) -> list[UserModel]: ...
