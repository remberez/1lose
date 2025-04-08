import typing

from sqlalchemy import ForeignKey, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, IntegerIDMixin, DateCreatedUpdatedMixin, UpdatedByMixin

if typing.TYPE_CHECKING:
    from core.models import MatchModel
    from core.models import MapModel
    from core.models import UserModel
    from core.models import BetModel


class OutComeModel(Base, IntegerIDMixin):
    __tablename__ = "outcome"

    name: Mapped[str] = mapped_column(String(32))
    coefficient: Mapped[float] = mapped_column(Numeric(10, 2))


class EventModel(Base, IntegerIDMixin, DateCreatedUpdatedMixin, UpdatedByMixin):
    __tablename__ = "event"

    match_id: Mapped[int] = mapped_column(ForeignKey("match.id", ondelete="CASCADE"))
    map_id: Mapped[int] = mapped_column(ForeignKey("map.id", ondelete="CASCADE"), nullable=True)
    name: Mapped[str] = mapped_column(String(32))
    first_outcome_id = mapped_column(ForeignKey("outcome.id"))
    second_outcome_id = mapped_column(ForeignKey("outcome.id"))

    match: Mapped["MatchModel"] = relationship(back_populates="events")
    map: Mapped["MapModel"] = relationship(back_populates="events")
    first_outcome: Mapped["OutComeModel"] = relationship(foreign_keys=first_outcome_id)
    second_outcome: Mapped["OutComeModel"] = relationship(foreign_keys=second_outcome_id)
    updated_by_r: Mapped["UserModel"] = relationship(back_populates="events_updated")
    bets: Mapped[list["BetModel"]] = relationship(back_populates="event")
