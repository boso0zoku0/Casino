from sqlalchemy.ext.asyncio import AsyncSession

from core.crud.players import add_player
from core.models import db_helper
from core.models.players import Players
from fastapi import APIRouter, Depends, status, Request

from core.schemas import PlayersPost
from core.schemas.players import PlayersGet

router = APIRouter()


@router.post("/player", name="player:join")
async def join_player(
    player: PlayersPost, session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await add_player(player=player, session=session)


# @router.post("/add-in-playmate", response_model=status.HTTP_201_CREATED)
# def add_in_playmate(request: Request, session: AsyncSession = Depends(db_helper.session_dependency)):
