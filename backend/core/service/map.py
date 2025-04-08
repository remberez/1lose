from typing import Callable

from core.schema.map import MapUpdateSchema, MapCreateSchema
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork


class MapService:
    def __init__(
            self,
            uow_factory: Callable[[], UnitOfWork],
            permissions_service: UserPermissionsService
    ):
        self._permissions_service = permissions_service
        self._uow_factory = uow_factory

    async def list(self):
        async with self._uow_factory() as uow:
            return await uow.maps.list()

    async def get(self, map_id: int):
        async with self._uow_factory() as uow:
            return await uow.maps.get(map_id)

    async def delete(self, map_id: int, user_id: int):
        # TODO: При удалении карты, вернуть деньги на баланс.
        await self._permissions_service.verify_admin(user_id)

        async with self._uow_factory() as uow:
            await uow.maps.delete(map_id)

    async def update(self, map_id: int, user_id: int, map_data: MapUpdateSchema):
        await self._permissions_service.verify_admin_or_moderator(user_id)

        async with self._uow_factory() as uow:
            return await uow.maps.update(map_id, **map_data.model_dump(exclude_none=True))

    async def create(self, user_id: int, map_data: MapCreateSchema):
        await self._permissions_service.verify_admin_or_moderator(user_id)

        async with self._uow_factory() as uow:
            return await uow.maps.create(**map_data.model_dump())
