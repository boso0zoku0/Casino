from sqlalchemy import Float, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.models.base import Base

# from core.models import Players


class Playmate(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(ForeignKey("players.username"))
    bet: Mapped[int]
    in_game: Mapped[bool] = mapped_column(default=False)
