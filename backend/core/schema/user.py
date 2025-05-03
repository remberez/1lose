from fastapi_users import schemas
from pydantic import Field

from core.types.user_id import UserID
from decimal import Decimal
from core.const.user_role import UserRoleCodes


class UserReadSchema(schemas.BaseUser[UserID]):
    balance: Decimal = Field(max_digits=12, decimal_places=2)
    role_code: str


class UserCreateSchema(schemas.BaseUserCreate): ...


class UserUpdateSelfSchema(schemas.BaseUserUpdate):
    ...


class UserUpdateAdminSchema(schemas.BaseUserUpdate):
    balance: Decimal | None = Field(None, max_digits=12, decimal_places=2)
    role_code: str | None = None
