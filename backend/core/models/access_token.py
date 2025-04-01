from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTable,
    SQLAlchemyAccessTokenDatabase,
)
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from core.types.user_id import UserID
from .base import Base


class AccessTokenModel(Base, SQLAlchemyBaseAccessTokenTable[UserID]):
    user_id: Mapped[UserID] = mapped_column(
        Integer,
        ForeignKey("user.id", ondelete="cascade"),
        nullable=True,
    )

    @classmethod
    def get_db(cls, session: AsyncSession):
        # Возвращает экземпляр класса SQLAlchemyAccessTokenDatabase,
        # который является адаптером базы данных для SQLAlchemy.
        return SQLAlchemyAccessTokenDatabase(session, cls)
