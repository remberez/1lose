from core.exceptions.common import BusinessValidationError
from core.repository.event import AbstractEventRepository
from core.repository.map import AbstractMapRepository
from core.schema.event import EventCreateSchema, EventUpdateSchema
from core.service.user import UserPermissionsService


class EventService:
    def __init__(
            self,
            repository: AbstractEventRepository,
            map_repo: AbstractMapRepository,
            permissions_service: UserPermissionsService,
    ):
        self._repo = repository
        self._permission_service = permissions_service
        self._map_repo = map_repo

    async def list(self):
        return await self._repo.list()

    async def get(self, event_id: int):
        return await self._repo.get(event_id)

    async def delete(self, event_id: int, user_id: int):
        await self._permission_service.verify_admin(user_id)
        await self._repo.delete(event_id)

    async def update(self, event_id: int, user_id: int, event_data: EventUpdateSchema):
        await self._permission_service.verify_admin_or_moderator(user_id)
        return await self._repo.update(event_id, **event_data.model_dump(exclude_none=True))

    async def create(self, user_id: int, event_data: EventCreateSchema):
        await self._permission_service.verify_admin_or_moderator(user_id)
        map_match_id = await self._map_repo.get_match_id(event_data.map_id)

        if map_match_id != event_data.match_id:
            raise BusinessValidationError("Map does not belong to the specified match")

        return await self._repo.create(**event_data.model_dump(), updated_by=user_id)
