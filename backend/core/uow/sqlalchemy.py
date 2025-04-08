from requests import session

from .uow import UnitOfWork
from ..repository.user import UserSQLAlchemyRepository


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.session = None

    async def __aenter__(self):
        self.session = self.session_factory()
        return self

    async def __aexit__(self, exc_type, *_):
        if exc_type:
            await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
