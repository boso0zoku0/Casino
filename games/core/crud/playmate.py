from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated

from core.crud.players import add_player
from core.models.playmate import Playmate
from core.schemas import PlayersPost
from core.schemas.playmate import PlaymateGet
import jwt


async def create_player_playmate(
    session: AsyncSession,
    player: Annotated[PlayersPost, Depends(add_player)],
    player_id: PlayersPost,
):
    add_playment = Playmate(**player["username"])

    playment_init = add_player(player_id)
