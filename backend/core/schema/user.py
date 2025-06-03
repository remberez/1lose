import re

from pydantic import Field, BaseModel, EmailStr, field_validator, ConfigDict

from decimal import Decimal


class UserBaseSchema(BaseModel):
    email: EmailStr
    balance: Decimal = Field(max_digits=12, decimal_places=2)
    role_code: str
    is_active: bool
    is_verified: bool

    model_config = ConfigDict(from_attributes=True)


class UserReadSchema(UserBaseSchema):
    id: int


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str | None = None
    type: str = "Bearer"


class UserUpdateSelfSchema(BaseModel):
    email: EmailStr


class UserUpdateAdminSchema(BaseModel):
    balance: Decimal | None = Field(None, max_digits=12, decimal_places=2)
    role_code: str | None = None
    is_active: bool | None = None
    is_verified: bool | None = None


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
