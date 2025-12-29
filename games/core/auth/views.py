from fastapi import APIRouter, Response, Request, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, select
from core.auth.helper import helper_jwt
from core.auth.utils import (
    validate_auth_user,
    generate_user_token,
    entry_user,
)
from core.roulette.utils import (
    get_users,
)
from core.models import Players, db_helper
from core.schemas import PlayersPost, PlayersGet
from core.schemas.players import PlayersLogin

router = APIRouter(prefix="/auth", tags=["AuthJWT"])


@router.post("/registrations/", status_code=status.HTTP_201_CREATED)
async def primary_entry(
    response: Response,
    player: PlayersPost,
    session: AsyncSession = Depends(
        db_helper.session_dependency,
    ),
    session_id: str = Depends(generate_user_token),
):
    try:
        payload = player.model_dump()
        access_token = helper_jwt.encode_jwt(payload=payload)

        response.set_cookie(key="session_id", value=session_id, expires=2000)
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
        return f"Registration was successful: {player.username}"

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists",
        )


@router.post("/login/", status_code=status.HTTP_200_OK)
async def entry(
    response: Response,
    player: PlayersLogin,
    session_id=Depends(generate_user_token),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await validate_auth_user(
        username=player.username, password=player.password, session=session
    )

    player_payload = player.model_dump()
    access_token = helper_jwt.encode_jwt(payload=player_payload)

    response.set_cookie(
        key="session_id", value=session_id, samesite="none", secure=True
    )
    await session.execute(
        update(Players)
        .where(Players.password == player.password)
        .values(
            cookies=session_id,
            access_token=access_token,
        )
    )
    await session.commit()
    return f"Authentication was successful: {player.username}"


@router.post("/users-browsing/", status_code=status.HTTP_200_OK)
async def users_browsing(
    players_or_playmate: bool,
    session: AsyncSession = Depends(db_helper.session_dependency),
):

    return await get_users(players_or_playmate=players_or_playmate, session=session)
