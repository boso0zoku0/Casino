from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Players
from sqlalchemy.orm import selectinload, joinedload


async def join_roulette(session: AsyncSession, user_id: int, bet: int):
    get_user = select(Players.id, Players.username).where(Players.id == user_id)
    add_member = Playmate(...)