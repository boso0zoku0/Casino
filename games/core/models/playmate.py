from sqlalchemy import Float, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.models.base import Base

# from core.models import Players
from sqlalchemy.dialects.postgresql import TIMESTAMP


class Playmate(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(ForeignKey("players.password"), unique=True)
    bet: Mapped[int]
    in_game: Mapped[bool] = mapped_column(default=False)
    cookies: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )
