from typing import Annotated

from fastapi.params import Depends

from api.dependencies.services.uow import get_uow
from core.service.user import UserService, UserPermissionsService
from core.uow.uow import UnitOfWork


async def get_user_permissions_service(
    uow_factory: Annotated[UnitOfWork, Depends(get_uow)],
) -> UserPermissionsService:
    return UserPermissionsService(uow_factory=lambda: uow_factory)


async def get_user_service(
    uow_factory: Annotated[UnitOfWork, Depends(get_uow)],
    permissions_service: Annotated[UserPermissionsService, Depends(get_user_permissions_service)]
) -> UserService:
    return UserService(uow_factory=lambda: uow_factory, permissions_service=permissions_service)
