from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Players
from core.models.db_helper import db_helper
from core.schemas import PlayersPost


async def add_player(
    player: PlayersPost, session: AsyncSession = Depends(db_helper.session_dependency)
):
    stmt = Players(**player.model_dump())
    session.add(stmt)
    await session.commit()
    return stmt
