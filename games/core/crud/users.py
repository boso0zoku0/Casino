from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated

from core.models import db_helper, Players
from core.models.playmate import Playmate
from core.schemas import PlayersPost


async def add_player(
    player: PlayersPost, session: AsyncSession = Depends(db_helper.session_dependency)
):
    stmt = Players(**player.model_dump())
    session.add(stmt)
    await session.commit()
    return stmt


async def get_all_users(
    user: str, session: AsyncSession = Depends(db_helper.session_dependency)
):

    fetch_user = select(Players).where(Players.username == user)

    results = await session.execute(fetch_user)
    return results.scalars()


async def create_player_playmate(
    session: AsyncSession,
    player: Annotated[PlayersPost, Depends(add_player)],
    player_id: PlayersPost,
):
    add_playment = Playmate(**player["username"])

    playment_init = add_player(player_id)
