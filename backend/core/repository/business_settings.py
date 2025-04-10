from abc import ABC

from sqlalchemy import select

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
    async def get(self, settings_name: str) -> str:
        stmt = (
            select(BusinessSettings)
            .where(BusinessSettings.name == settings_name)
        )
        result = await self._session.execute(stmt)
        return result.scalar_one().value
