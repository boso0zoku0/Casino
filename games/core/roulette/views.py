from typing import Annotated, List

from fastapi import (
    APIRouter,
    Request,
    Depends,
    BackgroundTasks,
    HTTPException,
    status,
    Query,
    Path,
    Body,
    Cookie,
    Request,
    Response,
    Header,
    Form,
)
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.websockets import WebSocketDisconnect, WebSocket

from core.models import db_helper
from core.models.roulette import PhaseStatus
from core.roulette.utils import (
    get_cookies_create_playmate,
    generate_tickets_roulette,
    my_details,
    fetch_playmate,
    add_random_playmates,
    game_phase_control,
)

router = APIRouter(prefix="/roulette", tags=["Roulette"])


@router.post("/join")
async def game_join(
    request: Request,
    bet: int,
    background_task: BackgroundTasks,
    session: AsyncSession = Depends(db_helper.session_dependency),
):

    # task = await get_cookies_create_playmate(
    #     request=request,
    #     bet=bet,
    #     session=session,
    # )
    background_task.add_task(
        get_cookies_create_playmate, request=request, session=session, bet=bet
    )
    return "You have joined the game"


@router.get("/winner")
async def take_winner(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await generate_tickets_roulette(session=session)


@router.get("/about/me")
async def details(
    request: Request, session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await my_details(session=session, request=request)


@router.get("/fetch/phase-control")
async def phase_control(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await game_phase_control(session=session)


@router.get("/fetch/")
async def fetch_game(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await fetch_playmate(session=session)


@router.post("/debug/create/playmates")
async def debug_add_playmates(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await add_random_playmates(session=session)
