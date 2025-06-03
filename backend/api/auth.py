from typing import Annotated

from fastapi import APIRouter, Form
from fastapi.params import Depends
from fastapi.security import HTTPBearer

from api.dependencies.auth.current_user import CurrentUserRefresh
from api.dependencies.services.user import get_user_service
from core.config import settings
from core.schema.user import UserReadSchema, UserRegisterSchema, TokenSchema
from core.service.user import UserService

http_bearer = HTTPBearer(auto_error=False)
router = APIRouter(
    prefix=settings.api.auth,
    tags=["Auth"],
    dependencies=[Depends(http_bearer)]
)

@router.post("/register", response_model=UserReadSchema)
async def register_user(
        user_data: UserRegisterSchema,
        user_service: Annotated[UserService, Depends(get_user_service)]
):
    return await user_service.register(user_data)


@router.post("/login", response_model=TokenSchema)
async def jwt_auth(
        username: Annotated[str, Form()],
        password: Annotated[str, Form()],
        user_service: Annotated[UserService, Depends(get_user_service)]
):
    return await user_service.jwt_login(email=username, password=password)

@router.post("/refresh", response_model=TokenSchema)
async def refresh_jwt_token(
        user: CurrentUserRefresh,
        service: Annotated[UserService, Depends(get_user_service)]
):
    return await service.jwt_refresh(user)