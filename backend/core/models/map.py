import typing

from sqlalchemy import ForeignKey, ARRAY, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, IntegerIDMixin, DateCreatedUpdatedMixin

if typing.TYPE_CHECKING:
    from core.models import EATeamModel
    from core.models import MatchModel
    from core.models import EventModel


class MapModel(Base, IntegerIDMixin, DateCreatedUpdatedMixin):
    __tablename__ = "map"

    match_id: Mapped[int] = mapped_column(ForeignKey("match.id", ondelete="CASCADE"))
    score: Mapped[list[int]] = mapped_column(ARRAY(Integer))
    winner_id: Mapped[int] = mapped_column(ForeignKey("ea_team.id", ondelete="SET NULL"), nullable=True)

    winner: Mapped["EATeamModel"] = relationship()
    match: Mapped["MatchModel"] = relationship(back_populates="maps")
    events: Mapped["EventModel"] = relationship(back_populates="map")
