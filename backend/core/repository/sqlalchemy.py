from abc import ABC
from typing import Sequence

from sqlalchemy import select, insert, update, Column, delete, exists, Integer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from .abc import AbstractReadRepository, AbstractWriteRepository


"""
Для корректной работы методов, модель должна иметь поле id.
Для моделей со специфичным названием первичного ключа нужно переопределить методы.
"""


class SQLAlchemyAbstractRepository[Model: DeclarativeBase](ABC):
    """
    Интерфейс репозитория SQLAlchemy, от которого должны наследоваться все репозитории,
    использующие SQLAlchemy ORM.
    """

    def __init__(self, session: AsyncSession, model: type[Model]) -> None:
        self._session = session
        self._model = model


class SQLAlchemyAbstractReadRepository[Model: DeclarativeBase](
    AbstractReadRepository[Model],
    SQLAlchemyAbstractRepository,
    ABC,
):
    async def get(self, model_id: int) -> Model:
        return await self._session.get(self._model, model_id)

    async def list(self, *args, **kwargs) -> Sequence[Model]:
        stmt = select(self._model).where(**kwargs)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def is_exists(self, model_id: int) -> bool:
        model_pk: Column[Integer] = self._model.id
        stmt = select(exists().where(model_pk == model_id))
        return bool(await self._session.scalar(stmt))


class SQLAlchemyAbstractWriteRepository[Model: DeclarativeBase](
    AbstractWriteRepository[Model],
    SQLAlchemyAbstractRepository,
    ABC,
):
    async def create(self, **model_data) -> Model:
        stmt = insert(self._model).values(**model_data).returning(self._model)
        model = await self._session.execute(stmt)
        await self._session.commit()
        return model.scalar_one()

    async def update(self, model_id: int, **data) -> Model:
        id_column: Column[int] = self._model.id
        stmt = (
            update(self._model)
            .where(id_column == model_id)
            .values(**data)
            .returning(self._model)
        )
        model = await self._session.execute(stmt)
        await self._session.commit()
        return model.scalar_one()

    async def delete(self, model_id: int) -> None:
        id_column: Column[int] = self._model.id
        stmt = delete(self._model).where(id_column == model_id)
        await self._session.execute(stmt)
        await self._session.commit()
