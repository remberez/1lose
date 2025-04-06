import typing

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, IntegerIDMixin

if typing.TYPE_CHECKING:
    from core.models import GameModel
    from core.models import MatchModel


class EATeamModel(Base, IntegerIDMixin):
    __tablename__ = "ea_team"
    name: Mapped[str] = mapped_column(String(32))
    game_id: Mapped[int] = mapped_column(ForeignKey("game.id"))

    game: Mapped["GameModel"] = relationship(back_populates="teams")
    matches_as_first_team: Mapped[list["MatchModel"]] = relationship(
        back_populates="first_team",
        foreign_keys="MatchModel.first_team_id"
    )
    matches_as_second_team: Mapped[list["MatchModel"]] = relationship(
        back_populates="second_team",
        foreign_keys="MatchModel.second_team_id"
    )