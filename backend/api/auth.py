from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from api.dependencies.services.user import get_user_service
from core.config import settings
from core.schema.user import UserReadSchema, UserRegisterSchema
from core.service.user import UserService

router = APIRouter(
    prefix=settings.api.auth,
    tags=["Auth"],
)


@router.post("/register", response_model=UserReadSchema)
async def register_user(
        user_data: UserRegisterSchema,
        user_service: Annotated[UserService, Depends(get_user_service)]
):
    return await user_service.register(user_data)
