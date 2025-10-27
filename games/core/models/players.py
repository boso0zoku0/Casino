from sqlalchemy import Float, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.models.base import Base


class Players(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=True)
    balance: Mapped[int] = mapped_column(default=0)
    email: Mapped[str] = mapped_column(nullable=True)
    years_active: Mapped[int]
