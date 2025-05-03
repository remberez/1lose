from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies.auth.current_user import current_user
from api.dependencies.services.user import get_user_service
from core.config import settings
from core.schema.user import UserReadSchema, UserUpdateSelfSchema, UserUpdateAdminSchema
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


@router.get("/", response_model=list[UserReadSchema])
async def user_list(
        service: Annotated[UserService, Depends(get_user_service)],
        user: Annotated[UserReadSchema, Depends(current_user)],
):
    return await service.list(user_id=user.id)


@router.patch("/me", response_model=UserReadSchema)
async def update_me(
        service: Annotated[UserService, Depends(get_user_service)],
        user: Annotated[UserReadSchema, Depends(current_user)],
        data: UserUpdateSelfSchema,
):
    return await service.update(target_user_id=user.id, user_data=data)


@router.patch("/{user_id}", response_model=UserReadSchema)
async def update_user(
        service: Annotated[UserService, Depends(get_user_service)],
        user: Annotated[UserReadSchema, Depends(current_user)],
        data: UserUpdateAdminSchema,
        user_id: int,
):
    return await service.update(user_id, data, user.id)
