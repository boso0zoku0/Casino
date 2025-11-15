from fastapi import APIRouter, Response, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, select

from core.auth.helper import helper_jwt
from core.auth.utils import (
    validate_auth_user,
    generate_user_token,
    entry_user,
)
from core.roulette.utils import get_cookies_create_playmate, generate_tickets_roulette
from core.models import Players, db_helper
from core.models.playmate import Playmate

from core.schemas import PlayersPost


router = APIRouter(prefix="/auth", tags=["AuthJWT"])


@router.post("/registrations/")
async def primary_entry(
    response: Response,
    player: PlayersPost,
    session: AsyncSession = Depends(
        db_helper.session_dependency,
    ),
    session_id: str = Depends(generate_user_token),
):

    player_payload = player.model_dump()
    access_token = helper_jwt.encode_jwt(payload=player_payload)

    response.set_cookie(key="session_id", value=session_id)
    await entry_user(session=session, player=player)
    await session.execute(
        update(Players)
        .where(Players.password == player.password)
        .values(
            cookies=session_id,
            access_token=access_token,
        )
    )
    await session.commit()
    return {"Hello": player.username}


@router.post("/login/")
async def entry(
    response: Response,
    player: PlayersPost,
    session_id=Depends(generate_user_token),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await validate_auth_user(
        username=player.username, password=player.password, session=session
    )

    player_payload = player.model_dump()
    access_token = helper_jwt.encode_jwt(payload=player_payload)

    response.set_cookie(key="session_id", value=session_id)
    await session.execute(
        update(Players)
        .where(Players.password == player.password)
        .values(
            cookies=session_id,
            access_token=access_token,
        )
    )
    await session.commit()
