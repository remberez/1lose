from typing import Callable

from core.exceptions.common import BusinessValidationError
from core.schema.event import EventCreateSchema, EventUpdateSchema, EventFilterSchema
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork
from core.uow.utils import with_uow


class EventService:
    def __init__(self, uow_factory: Callable[[], UnitOfWork]):
        self._uow_factory = uow_factory

    @with_uow
    async def list(self, filters: EventFilterSchema = None, uow: UnitOfWork = None):
        filters_data = filters.model_dump(exclude_none=True) if filters else {}
        return await uow.events.list(**filters_data)

    @with_uow
    async def get(self, event_id: int, uow: UnitOfWork = None):
        return await uow.events.get(event_id)

    @with_uow
    async def delete(self, event_id: int, user_id: int, uow: UnitOfWork = None):
        await uow.events.delete(event_id)

    @with_uow
    async def update(self, event_id: int, user_id: int, event_data: EventUpdateSchema, uow: UnitOfWork = None):
        return await uow.events.update(event_id, **event_data.model_dump(exclude_none=True))

    @with_uow
    async def create(self, user_id: int, event_data: EventCreateSchema, uow: UnitOfWork = None):
        map_match_id = await uow.maps.get_match_id(event_data.map_id)
        if map_match_id and map_match_id != event_data.match_id:
            raise BusinessValidationError("Map does not belong to the specified match")

        first_outcome_data = event_data.first_outcome.model_dump()
        second_outcome_data = event_data.second_outcome.model_dump()

        first_outcome = await uow.outcomes.create(**first_outcome_data)
        second_outcome = await uow.outcomes.create(**second_outcome_data)

        return await uow.events.create(
            **event_data.model_dump(exclude={"first_outcome", "second_outcome"}),
            updated_by=user_id,
            first_outcome_id=first_outcome.id,
            second_outcome_id=second_outcome.id,
        )
