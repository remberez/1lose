from datetime import datetime

from sqlalchemy import ForeignKey, ARRAY, Integer, SmallInteger, CheckConstraint, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, IntegerIDMixin, DateCreatedUpdatedMixin


class MatchModel(Base, DateCreatedUpdatedMixin, IntegerIDMixin):
    __tablename__ = "match"
    __table_args__ = (
        CheckConstraint(
            "first_team_id != second_team_id",
            name="check_teams_not_equal",
        ),
    )

    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournament.id", ondelete="CASCADE"))
    first_team_id: Mapped[int | None] = mapped_column(ForeignKey("ea_team.id", ondelete="SET NULL"))
    second_team_id: Mapped[int | None] = mapped_column(ForeignKey("ea_team.id", ondelete="SET NULL"))
    score: Mapped[list[int]] = mapped_column(ARRAY(Integer), nullable=True)
    best_of: Mapped[int] = mapped_column(SmallInteger())
    date_start: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True, default=None)
    date_end: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True, default=None)
