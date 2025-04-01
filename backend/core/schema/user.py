from fastapi_users import schemas
from pydantic import Field

from core.types.user_id import UserID
from decimal import Decimal


class UserReadSchema(schemas.BaseUser[UserID]):
    balance: Decimal = Field(max_digits=12, decimal_places=2)
    role_code: str


class UserCreateSchema(schemas.BaseUserCreate): ...


class UserUpdateSchema(schemas.BaseUserUpdate): ...
