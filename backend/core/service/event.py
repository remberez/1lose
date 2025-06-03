from typing import Callable

from core.exceptions.common import BusinessValidationError
from core.schema.event import EventCreateSchema, EventUpdateSchema, EventFilterSchema
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
        match_id_for_map = await uow.maps.get_match_id(event_data.map_id)
        if match_id_for_map and match_id_for_map != event_data.match_id:
            raise BusinessValidationError("Map does not belong to the specified match")

        event_model = await uow.events.create(
            **event_data.model_dump(exclude={"outcomes"}),
            updated_by=user_id,
        )
        for outcome in event_data.outcomes:
            model_outcome = await uow.outcomes.create(**outcome.model_dump())
            await uow.event_outcome.create_relationship(
                outcome_id=model_outcome.id,
                event_id=event_model.id,
            )
        return await uow.events.get(event_model.id)
