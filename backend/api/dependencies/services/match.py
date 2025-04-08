import typing
from typing import Annotated

from fastapi.params import Depends

from core.service.match import MatchService
from core.uow.uow import UnitOfWork
from .uow import get_uow
from .user import get_user_permissions_service

if typing.TYPE_CHECKING:
    from core.service.user import UserPermissionsService


async def match_service(
    uow_factory: Annotated[UnitOfWork, Depends(get_uow)],
    permissions_service: Annotated["UserPermissionsService", Depends(get_user_permissions_service)],
) -> MatchService:
    return MatchService(
        permissions_service=permissions_service,
        uow_factory=lambda: uow_factory,
    )
