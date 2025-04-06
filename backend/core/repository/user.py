from abc import ABC

from black.nodes import TypeVar
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
    ...


class UserSQLAlchemyRepository(
    SQLAlchemyAbstractReadRepository[UserModel],
    SQLAlchemyAbstractWriteRepository[UserModel],
    AbstractUserRepository,
): ...
