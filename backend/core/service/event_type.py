from typing import Callable

from core.exceptions.common import NotFoundError
from core.schema.event_type import EventTypeCreateSchema
from core.uow.uow import UnitOfWork
from core.uow.utils import with_uow


class EventTypeService:
    def __init__(self, uow_factory: Callable[[], UnitOfWork]):
        self._uow_factory = uow_factory

    @staticmethod
    async def _get_or_404(code: str, uow: UnitOfWork):
        event_type = await uow.event_type.get(code)
        if event_type:
            return event_type
        raise NotFoundError(f"Event type with {code} code not found.")

    @with_uow
    async def create(self, type_data: EventTypeCreateSchema, uow: UnitOfWork = None):
        event_type = await uow.event_type.create(**type_data.model_dump())
        return await self._get_or_404(event_type.code, uow)

    @with_uow
    async def get(self, code: str, uow: UnitOfWork = None):
        return await self._get_or_404(code, uow)
