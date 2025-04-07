from core.repository.event import AbstractEventRepository
from core.service.user import UserPermissionsService


class EventRepository:
    def __init__(
            self,
            repository: AbstractEventRepository,
            permissions_service: UserPermissionsService,
    ):
        self._repo = repository
        self._permission_service = permissions_service

    async def list(self):
        return await self._repo.list()

    async def get(self, map_id: int):
        return await self._repo.get(map_id)

    async def delete(self, map_id: int, user_id: int):
        await self._permission_service.verify_admin(user_id)
        await self._repo.delete(map_id)

    async def update(self, map_id: int, user_id: int, map_data):
        await self._permission_service.verify_admin_or_moderator(user_id)
        return await self._repo.update(map_id, **map_data.model_dump(exclude_none=True))

    async def create(self, user_id: int, map_data):
        await self._permission_service.verify_admin_or_moderator(user_id)
        return await self._repo.create(**map_data.model_dump())
