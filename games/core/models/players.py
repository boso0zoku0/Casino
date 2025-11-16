from sqlalchemy import Float, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.models.base import Base

from sqlalchemy.dialects.postgresql import TIMESTAMP


class Players(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False, unique=True)
    balance: Mapped[int] = mapped_column(default=0, nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)
    years_active: Mapped[int] = mapped_column(default=0, nullable=True)
    cookies: Mapped[str] = mapped_column(nullable=True)
    access_token: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )
