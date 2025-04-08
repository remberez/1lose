from typing import Annotated

from fastapi.params import Depends

from core.service.team import EATeamService
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork
from .uow import get_uow
from .user import get_user_permissions_service


async def get_ea_team_service(
    uow_factory: Annotated[UnitOfWork, Depends(get_uow)],
    permissions_service: Annotated[UserPermissionsService, Depends(get_user_permissions_service)],
) -> EATeamService:
    return EATeamService(
        permissions_service=permissions_service,
        uow_factory=lambda: uow_factory,
    )
