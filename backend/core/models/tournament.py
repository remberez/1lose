import typing

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, IntegerIDMixin, DateCreatedUpdatedMixin

if typing.TYPE_CHECKING:
    from core.models import GameModel


class TournamentModel(Base, IntegerIDMixin, DateCreatedUpdatedMixin):
    __tablename__ = "tournament"

    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str]
    game_id: Mapped[int] = mapped_column(ForeignKey("game.id"))

    game: Mapped["GameModel"] = relationship(back_populates="tournaments")
