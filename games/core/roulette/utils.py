import random

from fastapi import Depends, HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.requests import Request

from core.models import db_helper, Players
from core.models.playmate import Playmate


async def get_users(
    players_or_playmate: bool,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    if players_or_playmate:
        stmt = select(Players).order_by(Players.id)
        res = await session.execute(stmt)
        result = res.scalars().all()
        return result

    stmt = select(Playmate).order_by(Playmate.id)
    res = await session.execute(stmt)
    result = res.scalars().all()
    return result


async def get_randon_user(
    players_or_playmate: bool,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    if players_or_playmate:
        stmt = select(Players).order_by(Players.id)
        res = await session.execute(stmt)
        result = res.scalars().all()
        return result

    stmt = select(Playmate).order_by(Playmate.id)
    res = await session.execute(stmt)
    result = res.scalars().all()
    return result


async def get_cookies_create_playmate(
    request: Request,
    bet: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    cookies_get = request.cookies.get("session_id")
    stmt = select(Players).where(Players.cookies == cookies_get)
    result = await session.execute(stmt)
    players = result.scalars().first()

    # if players.username and players.password:
    #     raise HTTPException(
    #         status_code=status.HTTP_409_CONFLICT, detail="Bet has already been placed"
    #     )
    if cookies_get is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    new_playmate = Playmate(
        username=str(players.username),
        password=str(players.password),
        bet=bet,
        cookies=cookies_get,
    )
    session.add(new_playmate)
    await session.commit()
    return "ok"


async def winner_choice(tickets: int):
    return random.randint(0, tickets)


async def generate_tickets_roulette(
    request: Request,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    cookies_get = request.cookies.get("session_id")

    stmt_bets = select(Playmate.bet)
    execute_bets = await session.execute(stmt_bets)
    bets_list = execute_bets.scalars().all()
    sum_bets = sum(bets_list)

    stmt_playmates = select(Playmate.id)
    execute_playmates = await session.execute(stmt_playmates)
    user_ids = execute_playmates.scalars().all()

    win = await winner_choice(sum_bets)
    stmt = select(Playmate.username, Playmate.bet)
    res = await session.execute(stmt)
    users_bets = res.all()

    cumulative_bet = 0
    win_user = None
    win_ticket = None

    for playmate in users_bets:
        cumulative_bet += playmate[1]

        # if playmate[1] >= cumulative_bet:
        #     continue

        if cumulative_bet >= win:
            win_user = playmate[0]
            win_ticket = playmate[1]
            await session.execute(
                update(Playmate)
                .where(Playmate.username == win_user)
                .values(bet=sum_bets)
            )
            await session.execute(
                update(Playmate).where(Playmate.username != win_user).values(bet=0)
            )
            await session.commit()
            other_players = users_bets[:]
            await session.execute(delete(Playmate))
            await session.commit()
            return (
                {
                    "Winner": win_user,
                    "Winning ticket": win,
                    "All bets": sum_bets,
                    "All Players": str(other_players),
                },
            )

    # stmt = delete(Playmate)
    # await session.execute(delete(Playmate))
    await session.commit()
