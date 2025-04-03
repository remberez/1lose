import typing

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, IntegerIDMixin

if typing.TYPE_CHECKING:
    from core.models import GameModel


class EATeamModel(Base, IntegerIDMixin):
    __tablename__ = "ea_team"
    name: Mapped[str] = mapped_column(String(32))
    game_id: Mapped[int] = mapped_column(ForeignKey("game.id"))

    game: Mapped["GameModel"] = relationship(back_populates="teams")
