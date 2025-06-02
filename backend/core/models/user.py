import typing
from decimal import Decimal

from sqlalchemy import (
    Numeric,
    CheckConstraint,
    String,
    ForeignKey,
    text, Boolean,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from .base import (
    Base,
    IntegerIDMixin,
    DateCreatedUpdatedMixin,
)

if typing.TYPE_CHECKING:
    from core.models import EventModel
    from core.models import BetModel


class UserRoleModel(Base):
    __tablename__ = "user_role"

    code: Mapped[str] = mapped_column(String(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(20))

    users: Mapped[list["UserModel"]] = relationship(back_populates="role")


class UserModel(
    Base, DateCreatedUpdatedMixin, IntegerIDMixin
):
    __table_args__ = (CheckConstraint("balance >= 0", name="non_negative_balance"),)
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    balance: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=Decimal("0.00"))
    role_code: Mapped[str] = mapped_column(
        ForeignKey("user_role.code"), server_default=text("'user'")
    )

    role: Mapped["UserRoleModel"] = relationship(back_populates="users")
    events_updated: Mapped[list["EventModel"]] = relationship(back_populates="updated_by_r")
    bets: Mapped[list["BetModel"]] = relationship(back_populates="user")
