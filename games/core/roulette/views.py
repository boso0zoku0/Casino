from fastapi import (
    APIRouter,
    Response,
    Request,
    Depends,
    BackgroundTasks,
    HTTPException,
    status,
)
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, Players
from core.roulette.utils import get_cookies_create_playmate, generate_tickets_roulette


async def my_details(
    request: Request, session: AsyncSession = Depends(db_helper.session_dependency)
):
    get_cookies = request.cookies.get("session_id")
    if get_cookies:
        stmt = select(Players).where(Players.cookies == get_cookies)
        execute_stmt = await session.execute(stmt)
        user = execute_stmt.scalars().all()
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Not logged in"
    )


router = APIRouter(prefix="/roulette", tags=["Roulette"])


@router.post("/join")
async def game_join(
    request: Request,
    bet: int,
    # background_task: BackgroundTasks,
    session: AsyncSession = Depends(db_helper.session_dependency),
):

    task = await get_cookies_create_playmate(
        request=request,
        bet=bet,
        session=session,
    )
    # background_task.add_task(task)
    return "You have joined the game"


@router.post("/winner")
async def take_winner(
    request: Request,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await generate_tickets_roulette(session=session, request=request)


@router.get("/about/me")
async def my_details(
    request: Request, session: AsyncSession = Depends(db_helper.session_dependency)
):
    get_cookies = request.cookies.get("session_id")
    if get_cookies:
        stmt = select(Players).where(Players.cookies == get_cookies)
        execute_stmt = await session.execute(stmt)
        user = execute_stmt.scalars().first()
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Not logged in"
    )
