import typing
from decimal import Decimal
from enum import Enum

from sqlalchemy import ForeignKey, Numeric, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, Relationship, relationship

from .base import Base, IntegerIDMixin, DateCreatedUpdatedMixin
from ..const.bet_status import BetStatus

if typing.TYPE_CHECKING:
    from core.models import UserModel
    from core.models import EventModel


class BetModel(Base, IntegerIDMixin, DateCreatedUpdatedMixin):
    __tablename__ = "bet"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="SET NULL"))
    event_id: Mapped[int] = mapped_column(ForeignKey("event.id", ondelete="CASCADE"))
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    coefficient: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    possible_gain: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    bet_status: Mapped[BetStatus] = mapped_column(SQLEnum(BetStatus))

    user: Mapped["UserModel"] = Relationship(back_populates="bets")
    event: Mapped["EventModel"] = relationship(back_populates="bets")
