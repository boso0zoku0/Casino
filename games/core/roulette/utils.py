import logging
import random

from fastapi import Depends, HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.sql import func
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.requests import Request

from core.models import db_helper, Players
from core.models.playmate import Playmate

log = logging.getLogger(__name__)


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


async def get_cookies_create_playmate(
    request: Request,
    bet: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    cookies_get = request.cookies.get("session_id")
    stmt = select(Players).where(Players.cookies == cookies_get)
    result = await session.execute(stmt)
    players = result.scalars().first()

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
    log.info(f"Joined playmate - %s; bet - %s", new_playmate.username, new_playmate.bet)
    session.add(new_playmate)
    await session.commit()


async def winner_choice(tickets: int):
    return random.randint(0, tickets)


async def generate_tickets_roulette(
    request: Request,
    session: AsyncSession = Depends(db_helper.session_dependency),
):

    stmt = select(Playmate.username, Playmate.bet)
    execute_stmt = await session.execute(stmt)
    data_playmates = execute_stmt.fetchall()
    sum_bets = sum([user.bet for user in data_playmates])

    win = await winner_choice(sum_bets)

    stmt = select(Playmate.username, Playmate.bet)
    res = await session.execute(stmt)
    users_bets = res.all()

    if len(data_playmates) <= 1:
        return "Wait for players to connect to your room"

    cumulative_bet = 0

    for playmate in users_bets:
        cumulative_bet += playmate[1]

        if cumulative_bet >= win:
            win_user = playmate[0]

            stmt = (
                select(func.sum(Playmate.bet).label("bet"), Playmate.username)
                .where(Playmate.username == win_user)
                .group_by(Playmate.username)
            )
            exec_stmt = await session.execute(stmt)
            bet_winner = exec_stmt.scalars().all()
            bet_win = bet_winner[0]

            await session.execute(
                update(Playmate)
                .where(Playmate.username == win_user)
                .values(bet=sum_bets)
            )

            await session.execute(
                update(Playmate).where(Playmate.username != win_user).values(bet=0)
            )

            other_players = users_bets[:]
            all_players_debug = []

            for user in other_players:
                if user[0] not in all_players_debug:
                    all_players_debug.append(user)
            all_players = aggregate_tuples(all_players_debug)

            await session.execute(delete(Playmate))
            await session.commit()

            chance_win = round(((bet_win / sum_bets) * 100), 2)
            return (
                {
                    "Winner": win_user,
                    # "Winner tickets": bet_winner,  # отображается вся сумма победителя, задумка иная - выигрышный билет(эти данные вывожу в Ticket win возможно данное поле стоит уддалить из за не надобности
                    "Chance": f"{chance_win} %",
                    "Ticket win": win,
                    "All bets": sum_bets,
                    "All Players": str(all_players),
                    "All players debug": str(all_players_debug),
                },
            )

    await session.commit()


def aggregate_tuples(data: list) -> list:
    result_dict = {}
    for key, value in data:
        if key not in result_dict:
            result_dict[key] = value
        else:
            result_dict[key] += value

    return list(result_dict.items())
