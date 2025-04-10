from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class BusinessSettings(Base):
    __tablename__ = "business_settings"

    name: Mapped[str] = mapped_column(primary_key=True)
    value: Mapped[str]
