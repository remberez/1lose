from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.user import UserReadSchema, UserCreateSchema, UpdateBalanceSchema
from core.service.user import UserService
from .dependencies.auth.backend import auth_backend
from .dependencies.auth.current_user import current_user
from .dependencies.auth.fastapi_users import fastapi_users
from .dependencies.services.user import get_user_service

router = APIRouter(
    prefix=settings.api.auth,
    tags=["Auth"],
)

# login, logout
router.include_router(
    router=fastapi_users.get_auth_router(auth_backend),
)

# register
router.include_router(
    router=fastapi_users.get_register_router(UserReadSchema, UserCreateSchema),
)

router.include_router(
    router=fastapi_users.get_verify_router(UserReadSchema),
)


@router.get("/me", response_model=UserReadSchema)
async def get_me(user: Annotated[UserReadSchema, Depends(current_user)]):
    return user


@router.get("/{user_id}", response_model=UserReadSchema)
async def get_user(
    user_id: int,
    service: Annotated[UserService, Depends(get_user_service)],
):
    return await service.get(user_id)


@router.patch("/{user_id}", response_model=UpdateBalanceSchema)
async def update_balance(
        user_id: int,
        service: Annotated[UserService, Depends(get_user_service)],
        value: UpdateBalanceSchema,
        user: Annotated[UserReadSchema, Depends(current_user)],
):
    return UpdateBalanceSchema(balance=await service.update_balance(user_id, user.id, value.balance))


@router.get("/", response_model=list[UserReadSchema])
async def user_list(
        service: Annotated[UserService, Depends(get_user_service)],
        user: Annotated[UserReadSchema, Depends(current_user)],
):
    return await service.list(user_id=user.id)
