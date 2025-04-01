from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)
from datetime import datetime


class Base(DeclarativeBase):
    pass


class IntegerIDMixin:
    id: Mapped[int] = mapped_column(primary_key=True)


class DateCreatedUpdatedMixin:
    created_at: Mapped[datetime] = mapped_column(default=datetime.now, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now, onupdate=datetime.now, nullable=True
    )
