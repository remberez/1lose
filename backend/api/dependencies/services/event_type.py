from typing import Annotated

from fastapi import Depends

from api.dependencies.services.uow import get_uow
from core.service.event_type import EventTypeService
from core.uow.uow import UnitOfWork


async def get_event_type_service(
        uow_factory: Annotated[UnitOfWork, Depends(get_uow)],
):
    return EventTypeService(uow_factory=lambda: uow_factory)
