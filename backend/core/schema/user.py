import re

from fastapi_users import schemas
from pydantic import Field, BaseModel, EmailStr, field_validator

from core.types.user_id import UserID
from decimal import Decimal


class UserBaseSchema(BaseModel):
    email: EmailStr
    balance: Decimal = Field(max_digits=12, decimal_places=2)
    role_code: str
    is_active: bool
    is_verified: bool


class UserReadSchema(UserBaseSchema):
    id: int


class TokenSchema(BaseModel):
    access: str
    refresh: str | None = None
    type: str = "Bearer"


class UserUpdateSelfSchema(schemas.BaseUserUpdate):
    ...


class UserUpdateAdminSchema(schemas.BaseUserUpdate):
    balance: Decimal | None = Field(None, max_digits=12, decimal_places=2)
    role_code: str | None = None


class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)

    @field_validator("password")
    @classmethod
    def check_password(cls, password: str) -> str:
        if not re.fullmatch(r'^[\w!@#$%^&*()\-+=[\]{};:\'",.<>/?|\\~`]+$', password):
            raise ValueError("Password can only contain Latin letters, digits, and special characters")

        # Проверяем, что есть минимум 2 латинские буквы (в любом регистре)
        if len(re.findall(r'[a-zA-Z]', password)) < 2:
            raise ValueError("Password must contain at least 2 Latin letters")

        return password
