from fastapi import APIRouter

from core.schema.user import UserReadSchema, UserCreateSchema
from .dependencies.auth.backend import auth_backend
from .dependencies.auth.fastapi_users import fastapi_users
from core.config import settings

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
