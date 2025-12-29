import enum
import datetime
from sqlalchemy.orm import Mapped, mapped_column
from core.models.base import Base
from sqlalchemy import DateTime
from sqlalchemy.sql import func


class PhaseStatus(enum.Enum):
    BETTING = "betting"
    SPINNING = "spinning"
    RESULT = "result"


class Roulette(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    round_start_time: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )
    phase: Mapped[PhaseStatus] = mapped_column(default=PhaseStatus.BETTING)
    phase_duration: Mapped[int] = mapped_column(default=10)
    # created_date: Mapped[datetime.datetime] = mapped_column(
    #     DateTime(timezone=True), server_default=func.now()
    # )
