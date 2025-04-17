import typing
from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    ARRAY,
    Integer,
    SmallInteger,
    CheckConstraint,
    TIMESTAMP,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, IntegerIDMixin, DateCreatedUpdatedMixin

if typing.TYPE_CHECKING:
    from core.models import TournamentModel
    from core.models import EATeamModel
    from core.models import MapModel
    from core.models import EventModel
    from core.models import GameModel


class MatchModel(Base, DateCreatedUpdatedMixin, IntegerIDMixin):
    __tablename__ = "match"
    __table_args__ = (
        CheckConstraint(
            "first_team_id != second_team_id",
            name="check_teams_not_equal",
        ),
    )

    tournament_id: Mapped[int] = mapped_column(
        ForeignKey("tournament.id", ondelete="CASCADE")
    )
    first_team_id: Mapped[int | None] = mapped_column(
        ForeignKey("ea_team.id", ondelete="SET NULL")
    )
    second_team_id: Mapped[int | None] = mapped_column(
        ForeignKey("ea_team.id", ondelete="SET NULL")
    )
    score: Mapped[list[int]] = mapped_column(ARRAY(Integer), nullable=True)
    best_of: Mapped[int] = mapped_column(SmallInteger())
    date_start: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True, default=None
    )
    date_end: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True, default=None
    )
    game_id: Mapped[int] = mapped_column(ForeignKey("game.id", ondelete="CASCADE"), nullable=True)
    win_event_id: Mapped[int] = mapped_column(ForeignKey("event.id", ondelete="CASCADE"), nullable=True)

    tournament: Mapped["TournamentModel"] = relationship(back_populates="matches")
    first_team: Mapped["EATeamModel"] = relationship(
        back_populates="matches_as_first_team",
        foreign_keys="MatchModel.first_team_id",
    )
    second_team: Mapped["EATeamModel"] = relationship(
        back_populates="matches_as_second_team",
        foreign_keys="MatchModel.second_team_id",
    )
    maps: Mapped[list["MapModel"]] = relationship(back_populates="match")
    events: Mapped[list["EventModel"]] = relationship(back_populates="match")
    game: Mapped["GameModel"] = relationship(back_populates="matches")
