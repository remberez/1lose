from typing import Annotated

from fastapi.params import Depends

from core.service.event import EventService
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork
from .uow import get_uow
from .user import get_user_permissions_service


async def event_service(
        uow_factory: Annotated[UnitOfWork, Depends(get_uow)],
        permission_service: Annotated[UserPermissionsService, Depends(get_user_permissions_service)]
) -> EventService:
    return EventService(uow_factory=lambda: uow_factory, permissions_service=permission_service)
