import typing
from decimal import Decimal
from typing import TypeVar

from core.auth.jwt import create_access_token, create_refresh_token
from core.const.user_role import UserRoleCodes
from core.exceptions.common import NotFoundError, AlreadyExistsError
from core.exceptions.user_exc import UserPermissionError
from core.models import UserModel
from core.schema.user import UserUpdateSelfSchema, UserUpdateAdminSchema, UserRegisterSchema, TokenSchema, \
    UserReadSchema
from core.uow.uow import UnitOfWork
from core.uow.utils import with_uow
from core.utils.auth import hash_password, validate_password

UserModelT = TypeVar("UserModelT")


class UserService:
    def __init__(
        self,
        uow_factory: typing.Callable[[], UnitOfWork],
        permissions_service: "UserPermissionsService",
    ):
        self._uow_factory = uow_factory
        self._permissions_service = permissions_service

    @with_uow
    async def register(self, user_data: UserRegisterSchema, uow: UnitOfWork):
        if await uow.users.get_user_by_email(email=str(user_data.email)):
            raise AlreadyExistsError(f"Email {user_data.email} already exists")

        hashed_password = hash_password(user_data.password).decode()
        user_model = await uow.users.create(
            email=str(user_data.email),
            hashed_password=hashed_password
        )
        return user_model

    async def is_exists(self, user_id: int, uow: UnitOfWork):
        if not await uow.users.is_exists(user_id):
            raise NotFoundError(f"User {user_id} not found")

    @with_uow
    async def get(self, user_id: int, uow: UnitOfWork) -> UserModelT:
        await self.is_exists(user_id, uow)
        return await uow.users.get(user_id)

    @with_uow
    async def update_balance(self, user_id: int, target_user_id: int, balance: Decimal, uow: UnitOfWork):
        return await uow.users.update_user_balance(target_user_id, balance)

    @with_uow
    async def list(self, user_id: int, uow: UnitOfWork):
        return await uow.users.list()

    @with_uow
    async def admin_update(
            self,
            target_user_id: int,
            user_data: UserUpdateAdminSchema,
            uow: UnitOfWork = None,
    ):
        return await uow.users.update(target_user_id, **user_data.model_dump(exclude_none=True))


    @with_uow
    async def update(
        self,
        target_user_id: int,
            user_data: UserUpdateSelfSchema,
        user_id: int | None = None,
        uow: UnitOfWork = None,
    ):
        if user_id and user_id != target_user_id:
            await self._permissions_service.verify_admin(user_id)

        if user_data.email:
            user_same_email = await uow.users.get_user_by_email(str(user_data.email))
            if user_same_email:
                raise AlreadyExistsError(f"User with email {user_data.email!r} already exists")

        return await uow.users.update(target_user_id, **user_data.model_dump(exclude_none=True))

    @with_uow
    async def jwt_login(self, email: str, password: str, uow: UnitOfWork):
        user_model: UserModel = await uow.users.get_user_by_email(email)
        if not (user := user_model):
            raise NotFoundError("Invalid username or password")

        if validate_password(password, user.hashed_password.encode()):
            return TokenSchema(
                access_token=create_access_token(UserReadSchema.model_validate(user_model)),
                refresh_token=create_refresh_token(UserReadSchema.model_validate(user_model)),
            )
        raise NotFoundError("Invalid username or password")


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
