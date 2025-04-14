from typing import Callable

from core.schema.business_settings import BusinessSettingsUpdateSchema
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork


class BusinessSettingsService:
    def __init__(
            self,
            uow: Callable[[], UnitOfWork],
            permissions_service: UserPermissionsService,
    ):
        self._uow_factory = uow
        self._permissions_service = permissions_service

    async def list(self, user_id: int):
        await self._permissions_service.verify_admin(user_id)
        async with self._uow_factory() as uow:
            return await uow.business_settings.list()

    async def get(self, settings_name: str, user_id: int):
        await self._permissions_service.verify_admin(user_id)
        async with self._uow_factory() as uow:
            return await uow.business_settings.get(settings_name)

    async def create(self, user_id):
        await self._permissions_service.verify_admin(user_id)
        async with self._uow_factory() as uow:
            return await uow.business_settings.create()

    async def delete(self, settings_name: str, user_id: int):
        await self._permissions_service.verify_admin(user_id)
        async with self._uow_factory() as uow:
            return await uow.business_settings.delete(settings_name)

    async def update(self, settings_name: str, settings_data: BusinessSettingsUpdateSchema, user_id: int):
        await self._permissions_service.verify_admin(user_id)
        async with self._uow_factory() as uow:
            return await uow.business_settings.update(settings_name, **settings_data.model_dump())
