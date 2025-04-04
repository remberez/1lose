import typing

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, IntegerIDMixin

if typing.TYPE_CHECKING:
    from .team import EATeamModel
    from core.models.tournament import TournamentModel


class GameModel(Base, IntegerIDMixin):
    __tablename__ = "game"

    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str]

    teams: Mapped[list["EATeamModel"]] = relationship(back_populates="game")
    tournaments: Mapped[list["TournamentModel"]] = relationship(back_populates="game")
