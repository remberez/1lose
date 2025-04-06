from functools import wraps
from typing import Callable, TypeVar, Any, Coroutine

from typing_extensions import ParamSpec

from core.const.user_role import UserRoleCodes
from core.exceptions.common import NotFoundError
from core.exceptions.user_exc import UserPermissionError
from core.repository.user import AbstractUserRepository

UserModelT = TypeVar("UserModelT")
P = ParamSpec("P")
R = TypeVar("R")


class UserService:
    def __init__(self, repository: AbstractUserRepository):
        self._repository = repository

    async def is_exists(self, user_id: int):
        if not await self._repository.is_exists(user_id):
            raise NotFoundError(f"User {user_id} not found")

    async def get(self, user_id: int) -> UserModelT:
        await self.is_exists(user_id)
        return await self._repository.get(user_id)


class UserPermissionsService:
    def __init__(self, user_repository: AbstractUserRepository):
        self._user_repository = user_repository

    async def verify_admin_or_moderator(self, user_id: int) -> None:
        user = await self._user_repository.get(user_id)
        if user.role_code not in (
            UserRoleCodes.ADMIN.value,
            UserRoleCodes.MODERATOR.value,
        ):
            raise UserPermissionError()

    async def verify_admin(self, user_id: int) -> None:
        user = await self._user_repository.get(user_id)

        if user.role_code != UserRoleCodes.ADMIN.value:
            raise UserPermissionError()
