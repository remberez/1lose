from typing import Annotated

from fastapi.params import Depends
from core.service.game import GameService
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork
from .user import get_user_permissions_service
from .uow import get_uow

async def get_game_service(
    permissions_service: Annotated[UserPermissionsService,Depends(get_user_permissions_service)],
    uow_factory: Annotated[UnitOfWork, Depends(get_uow)]
) -> GameService:
    return GameService(permissions_service=permissions_service, uow_factory=lambda: uow_factory)
