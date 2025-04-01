from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTable,
    SQLAlchemyAccessTokenDatabase,
)
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from core.types.user_id import UserID


class AccessTokenModel(Base, SQLAlchemyBaseAccessTokenTable[UserID]):
    user_id: Mapped[UserID] = mapped_column(
        Integer,
        ForeignKey("user.id", ondelete="cascade"),
        nullable=True,
    )

    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyAccessTokenDatabase(session, cls)
