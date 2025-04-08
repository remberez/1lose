import typing
from decimal import Decimal
from typing import TypeVar

from core.const.user_role import UserRoleCodes
from core.exceptions.common import NotFoundError
from core.exceptions.user_exc import UserPermissionError
from core.uow.uow import UnitOfWork

UserModelT = TypeVar("UserModelT")


class UserService:
    def __init__(
            self,
            uow_factory: typing.Callable[[], UnitOfWork],
            permissions_service: "UserPermissionsService",
    ):
        self._uow_factory = uow_factory
        self._permissions_service = permissions_service

    async def is_exists(self, user_id: int, uow: UnitOfWork):
        if not await uow.users.is_exists(user_id):
            raise NotFoundError(f"User {user_id} not found")

    async def get(self, user_id: int) -> UserModelT:
        async with self._uow_factory() as uow:
            await self.is_exists(user_id, uow)
            return await uow.users.get(user_id)

    async def update_balance(self, user_id: int, target_user_id: int, balance: Decimal):
        await self._permissions_service.verify_admin(user_id)

        async with self._uow_factory() as uow:
            return await uow.users.update_user_balance(target_user_id, balance)


class UserPermissionsService:
    def __init__(
            self,
            uow_factory: typing.Callable[[], UnitOfWork],
    ):
        self._uow_factory = uow_factory

    async def verify_admin_or_moderator(self, user_id: int) -> None:
        async with self._uow_factory() as uow:
            user = await uow.users.get(user_id)
            if user.role_code not in (
                    UserRoleCodes.ADMIN.value,
                    UserRoleCodes.MODERATOR.value,
            ):
                raise UserPermissionError()

    async def verify_admin(self, user_id: int) -> None:
        async with self._uow_factory() as uow:
            user = await uow.users.get(user_id)

            if user.role_code != UserRoleCodes.ADMIN.value:
                raise UserPermissionError()
