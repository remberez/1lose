from abc import ABC

from black.nodes import TypeVar
from core.repository.sqlalchemy import SQLAlchemyAbstractRepository, AbstractRepository
from core.models.user import UserModel

UserModelT = TypeVar("UserModelT")

class AbstractUserRepository(AbstractRepository[UserModel], ABC):
    # Специфичные методы для работы с пользователями.
    ...


class UserSQLAlchemyRepository(SQLAlchemyAbstractRepository, AbstractUserRepository):
    # Реализация репозитория с помощью SQLAlchemy.
    async def get(self, user_id: int) -> UserModel | None:
        return await self._session.get(UserModel, user_id)

    async def list(self, *args, **kwargs) -> list[UserModel]:
        ...

    async def delete(self, model_id: int) -> None:
        ...

    async def create(self, **data) -> UserModel | None:
        raise NotImplementedError()

    async def update(self, model_id: int, **data) -> UserModel:
        ...
