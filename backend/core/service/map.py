from typing import Callable

from core.schema.map import MapUpdateSchema, MapCreateSchema
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork
from core.uow.utils import with_uow


class MapService:
    def __init__(
        self,
        uow_factory: Callable[[], UnitOfWork],
        permissions_service: UserPermissionsService
    ):
        self._permissions_service = permissions_service
        self._uow_factory = uow_factory

    @with_uow
    async def list(self, uow: UnitOfWork):
        return await uow.maps.list()

    @with_uow
    async def get(self, map_id: int, uow: UnitOfWork):
        return await uow.maps.get(map_id)

    @with_uow
    async def delete(self, map_id: int, user_id: int, uow: UnitOfWork):
        # TODO: При удалении карты, вернуть деньги на баланс.
        await uow.maps.delete(map_id)

    @with_uow
    async def update(self, map_id: int, user_id: int, map_data: MapUpdateSchema, uow: UnitOfWork):
        return await uow.maps.update(map_id, **map_data.model_dump(exclude_none=True))

    @with_uow
    async def create(self, user_id: int, map_data: MapCreateSchema, uow: UnitOfWork):
        return await uow.maps.create(**map_data.model_dump())
