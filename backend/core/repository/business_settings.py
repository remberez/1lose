from abc import ABC

from sqlalchemy import select, delete, update, exists

from core.models import BusinessSettings
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractReadRepository, SQLAlchemyAbstractWriteRepository


class AbstractBusinessSettingsRepository[Model](
    AbstractReadRepository[Model],
    AbstractWriteRepository[Model],
    ABC,
):
    # Специфичные методы для работы с BusinessModel
    ...


class SQLAlchemyBusinessSettingsRepository(
    AbstractBusinessSettingsRepository[BusinessSettings],
    SQLAlchemyAbstractReadRepository,
    SQLAlchemyAbstractWriteRepository,
):
    async def get(self, settings_name: str) -> str | None:
        stmt = (
            select(BusinessSettings)
            .where(BusinessSettings.name == settings_name)
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def delete(self, settings_name: str) -> None:
        stmt = (
            delete(BusinessSettings)
            .where(BusinessSettings.name == settings_name)
        )
        await self._session.execute(stmt)

    async def update(self, settings_name: str, **data) -> BusinessSettings:
        stmt = (
            update(BusinessSettings)
            .where(BusinessSettings.name == settings_name)
            .values(**data)
            .returning(BusinessSettings)
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def is_exists(self, settings_name: str) -> bool:
        stmt = (
            select(
                exists().where(BusinessSettings.name == settings_name)
            )
        )
        return await self._session.scalar(stmt)
