from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)
from datetime import datetime


class Base(DeclarativeBase):
    pass


class DateCreatedUpdatedMixin:
    created_at: Mapped[datetime] = mapped_column(default=datetime.now, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now, nullable=True)
