from typing import Callable

from core.exceptions.common import BusinessValidationError
from core.schema.event import EventCreateSchema, EventUpdateSchema
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork


class EventService:
    def __init__(
            self,
            uow_factory: Callable[[], UnitOfWork],
            permissions_service: UserPermissionsService
    ):
        self._permissions_service = permissions_service
        self._uow_factory = uow_factory

    async def list(self):
        async with self._uow_factory() as uow:
            return await uow.events.list()

    async def get(self, event_id: int):
        async with self._uow_factory() as uow:
            return await uow.events.get(event_id)

    async def delete(self, event_id: int, user_id: int):
        await self._permissions_service.verify_admin(user_id)

        async with self._uow_factory() as uow:
            await uow.events.delete(event_id)

    async def update(self, event_id: int, user_id: int, event_data: EventUpdateSchema):
        await self._permissions_service.verify_admin_or_moderator(user_id)

        async with self._uow_factory() as uow:
            return await uow.events.update(event_id, **event_data.model_dump(exclude_none=True))

    async def create(self, user_id: int, event_data: EventCreateSchema):
        await self._permissions_service.verify_admin_or_moderator(user_id)

        async with self._uow_factory() as uow:
            map_match_id = await uow.maps.get_match_id(event_data.map_id)

            if map_match_id and map_match_id != event_data.match_id:
                raise BusinessValidationError("Map does not belong to the specified match")

            first_outcome_data = event_data.first_outcome.model_dump()
            second_outcome_data = event_data.second_outcome.model_dump()

            first_outcome = await uow.outcomes.create(**first_outcome_data)
            second_outcome = await uow.outcomes.create(**second_outcome_data)

            return await uow.events.create(
                **event_data.model_dump(
                    exclude={"first_outcome", "second_outcome"}
                ),
                updated_by=user_id,
                first_outcome_id=first_outcome.id,
                second_outcome_id=second_outcome.id,
            )
