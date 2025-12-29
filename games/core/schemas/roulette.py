from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class Roulette(BaseModel):
    created_at: datetime
    round_start_time: datetime
    phase: Literal["betting", "spinning", "result"] = "betting"
    phase_duration: int

    class Config:
        arbitrary_types_allowed = True
