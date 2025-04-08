from typing import Annotated

from fastapi.params import Depends

from core.service.map import MapService
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork
from .uow import get_uow
from .user import get_user_permissions_service


async def map_service(
        uow_factory: Annotated[UnitOfWork, Depends(get_uow)],
        permissions_service: Annotated[UserPermissionsService, Depends(get_user_permissions_service)],
) -> MapService:
    return MapService(
        uow_factory=lambda: uow_factory,
        permissions_service=permissions_service,
    )
