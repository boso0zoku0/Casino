from fastapi import APIRouter, Response, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.roulette.utils import get_cookies_create_playmate, generate_tickets_roulette

router = APIRouter(
    prefix="/roulette",
    tags=["Roulette"],
    dependencies=[Depends(get_cookies_create_playmate)],
)


@router.post("/join")
async def game_join(
    request: Request,
    bet: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await get_cookies_create_playmate(
        request=request,
        bet=bet,
        session=session,
    )


@router.post("/winner")
async def take_winner(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await generate_tickets_roulette(session=session)
