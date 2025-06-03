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

    bets: Mapped[list["BetModel"]] = relationship(back_populates="outcome")


class EventModel(Base, IntegerIDMixin, DateCreatedUpdatedMixin, UpdatedByMixin):
    __tablename__ = "event"

    match_id: Mapped[int] = mapped_column(ForeignKey("match.id", ondelete="CASCADE"))
    map_id: Mapped[int] = mapped_column(ForeignKey("map.id", ondelete="CASCADE"), nullable=True)
    name: Mapped[str] = mapped_column(String(32))

    match: Mapped["MatchModel"] = relationship(back_populates="events", foreign_keys=match_id)
    map: Mapped["MapModel"] = relationship(back_populates="events")
    updated_by_r: Mapped["UserModel"] = relationship(back_populates="events_updated")
    bets: Mapped[list["BetModel"]] = relationship(back_populates="event")
    match_as_win_event: Mapped["MatchModel"] = relationship(back_populates="win_event",
                                                            foreign_keys="MatchModel.win_event_id",
                                                            uselist=False)
    outcomes: Mapped[list["EventOutcomeModel"]] = relationship()


class EventOutcomeModel(Base):
    __tablename__ = "event_outcome"

    event_id: Mapped[int] = mapped_column(ForeignKey("event.id", ondelete="CASCADE"), primary_key=True)
    outcome_id: Mapped[int] = mapped_column(ForeignKey("outcome.id", ondelete="CASCADE"), primary_key=True)
