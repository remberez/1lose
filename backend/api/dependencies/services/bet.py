from typing import Annotated

from fastapi.params import Depends

from core.service.bet import BetService
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork
from .uow import get_uow
from .user import get_user_permissions_service


async def bet_service(
        uow_factory: Annotated[UnitOfWork, Depends(get_uow)],
        permission_service: Annotated[UserPermissionsService, Depends(get_user_permissions_service)]
) -> BetService:
    return BetService(uow_factory=lambda: uow_factory, permissions_service=permission_service)

