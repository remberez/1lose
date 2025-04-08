from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker

from core.models.db_helper import db_helper
from core.uow.sqlalchemy import SqlAlchemyUnitOfWork
from core.uow.uow import UnitOfWork


async def get_uow(
        session_factory: Annotated[async_sessionmaker, Depends(db_helper.get_session_maker)]
) -> UnitOfWork:
    return SqlAlchemyUnitOfWork(session_factory)
