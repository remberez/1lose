from typing import Annotated

from fastapi.params import Depends

from core.service.event import EventService
from core.uow.uow import UnitOfWork
from .uow import get_uow


async def event_service(
        uow_factory: Annotated[UnitOfWork, Depends(get_uow)],
) -> EventService:
    return EventService(uow_factory=lambda: uow_factory)
