from typing import Callable

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

    async def list(self):
        async with self._uow_factory() as uow:
            return await uow.business_settings.list()

    async def get(self, settings_name: str):
        async with self._uow_factory() as uow:
            return await uow.business_settings.get(settings_name)

    async def create(self, **data):
        ...

    async def delete(self, settings_name: str):
        ...

    async def update(self, settings_name: str):
        ...
