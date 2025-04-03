from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession
from .abc import AbstractWriteRepository, AbstractReadRepository


class SQLAlchemyAbstractRepository[Model](AbstractWriteRepository[Model], AbstractReadRepository[Model], ABC):
    """
    Интерфейс репозитория SQLAlchemy, от которого должны наследоваться все репозитории,
    использующие SQLAlchemy ORM.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session
