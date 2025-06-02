from typing import Callable

from core.exceptions.common import NotFoundError
from core.schema.business_settings import BusinessSettingsUpdateSchema, BusinessSettingsCreateSchema
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork
from core.uow.utils import with_uow


class BusinessSettingsService:
    def __init__(
            self,
            uow: Callable[[], UnitOfWork],
            permissions_service: UserPermissionsService,
    ):
        self._uow_factory = uow
        self._permissions_service = permissions_service

    async def _is_exists(self, settings_name: str, uow: UnitOfWork):
        if not await uow.business_settings.is_exists(settings_name):
            raise NotFoundError(f"Settings {settings_name} not found")

    @with_uow
    async def list(self, user_id: int, uow: UnitOfWork):
        return await uow.business_settings.list()

    @with_uow
    async def get(self, settings_name: str, user_id: int, uow: UnitOfWork):
        await self._is_exists(settings_name, uow)
        return await uow.business_settings.get(settings_name)

    @with_uow
    async def create(self, user_id: int, settings_data: BusinessSettingsCreateSchema, uow: UnitOfWork):
        return await uow.business_settings.create(**settings_data.model_dump())

    @with_uow
    async def delete(self, settings_name: str, user_id: int, uow: UnitOfWork):
        return await uow.business_settings.delete(settings_name)

    @with_uow
    async def update(self, settings_name: str, settings_data: BusinessSettingsUpdateSchema, user_id: int,
                     uow: UnitOfWork):
        await self._is_exists(settings_name, uow)
        return await uow.business_settings.update(
            settings_name,
            **settings_data.model_dump(exclude_none=True)
        )
