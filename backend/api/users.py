from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies.auth.current_user import current_user
from api.dependencies.services.user import get_user_service
from core.config import settings
from core.schema.user import UserReadSchema, UpdateBalanceSchema
from core.service.user import UserService

router = APIRouter(prefix=settings.api.users, tags=["Users"])

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
