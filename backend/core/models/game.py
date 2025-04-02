from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, IntegerIDMixin


class GameModel(Base, IntegerIDMixin):
    __tablename__ = "game"

    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str]
