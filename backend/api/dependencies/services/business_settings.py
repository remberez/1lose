from typing import Annotated

from fastapi.params import Depends

from core.service.business_settings import BusinessSettingsService
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork
from .uow import get_uow
from .user import get_user_permissions_service


async def business_settings(
        uow_factory: Annotated[UnitOfWork, Depends(get_uow)],
        permissions_service: Annotated[UserPermissionsService, Depends(get_user_permissions_service)],
) -> BusinessSettingsService:
    return BusinessSettingsService(uow=lambda: uow_factory, permissions_service=permissions_service)
