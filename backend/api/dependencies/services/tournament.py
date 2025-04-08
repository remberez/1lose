from typing import Annotated

from fastapi.params import Depends

from core.service.tournament import TournamentService
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork
from .uow import get_uow
from .user import get_user_permissions_service


async def get_tournament_service(
    uow_factory: Annotated[UnitOfWork, Depends(get_uow)],
    permission_service: Annotated[UserPermissionsService, Depends(get_user_permissions_service)],
) -> TournamentService:
    return TournamentService(
        permissions_service=permission_service, uow_factory=lambda: uow_factory
    )
