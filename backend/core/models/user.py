import typing

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy import (
    Numeric,
    CheckConstraint,
    String,
    ForeignKey,
    text,
)
from decimal import Decimal

from .base import (
    Base,
    IntegerIDMixin,
    DateCreatedUpdatedMixin,
)
from core.types.user_id import UserID

if typing.TYPE_CHECKING:
    from core.models import EventModel
    from core.models import BetModel


class UserRoleModel(Base):
    __tablename__ = "user_role"

    code: Mapped[str] = mapped_column(String(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(20))

    users: Mapped[list["UserModel"]] = relationship(back_populates="role")


class UserModel(
    Base, DateCreatedUpdatedMixin, IntegerIDMixin, SQLAlchemyBaseUserTable[UserID]
):
    __table_args__ = (CheckConstraint("balance >= 0", name="non_negative_balance"),)

    balance: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=Decimal("0.00"))
    role_code: Mapped[str] = mapped_column(
        ForeignKey("user_role.code"), server_default=text("'user'")
    )

    role: Mapped["UserRoleModel"] = relationship(back_populates="users")
    events_updated: Mapped[list["EventModel"]] = relationship(back_populates="updated_by_r")
    bets: Mapped[list["BetModel"]] = relationship(back_populates="user")


    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, cls)
