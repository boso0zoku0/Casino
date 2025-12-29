import logging
import random
from datetime import datetime, timezone

from fastapi import Depends, HTTPException
from sqlalchemy import select, insert, update, delete, desc
from sqlalchemy.engine import row
from sqlalchemy.sql import func
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse
from core.models import db_helper, Players
from core.models.playmate import Playmate
from core.models.roulette import Roulette, PhaseStatus

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
        photo=str(players.photo),
    )
    log.info(
        f"Joined playmate - %s; bet - %s;",
        new_playmate.username,
        new_playmate.bet,
    )
    session.add(new_playmate)
    await session.commit()


async def winner_choice(tickets: int):
    return random.randint(0, tickets)


async def generate_tickets_roulette(
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


async def fetch_playmate(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    stmt = select(Playmate.username, Playmate.bet, Playmate.photo)
    execute_stmt = await session.execute(stmt)
    rows = execute_stmt.fetchall()
    players = [{"username": item[0], "bet": item[1], "photo": item[2]} for item in rows]
    return players


async def add_random_playmates(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    stmt = insert(Playmate).values(
        [
            {
                "username": "debug1",
                "password": "debug1",
                "bet": 341,
                "cookies": None,
                "photo": "https://media.kasperskydaily.com/wp-content/uploads/sites/90/2016/05/06042126/joliepitt-1-1024x672.gif",
            },
            {
                "username": "debug2",
                "password": "debug2",
                "bet": 123,
                "cookies": None,
                "photo": None,
            },
            {
                "username": "debug3",
                "password": "debug3",
                "bet": 5555,
                "cookies": None,
                "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR50nslVVIO5ytPj8m68UcJKWeL6sP78vNp6Q&s",
            },
            {
                "username": "debug4",
                "password": "debug4",
                "bet": 7676,
                "cookies": None,
                "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVOKyGYskD1iNwq65qbNkkRYQ27_saVYG1Lw&s",
            },
        ]
    )
    await session.execute(stmt)
    # session.add(stmt)
    await session.commit()
    return "ok"


async def game_phase_control(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    stmt = select(Roulette).order_by(Roulette.created_at.desc()).limit(1)
    result = await session.execute(stmt)
    current_round = result.scalars().first()
    time_now = datetime.now(tz=timezone.utc)
    print(
        f"round_start_time: {current_round.round_start_time}, tzinfo: {current_round.round_start_time.tzinfo}"
    )

    if not current_round:
        init_round = Roulette(
            phase=PhaseStatus.BETTING,
            phase_duration=3,
            round_start_time=time_now,
        )
        session.add(init_round)
        session.expire(init_round)
        await session.commit()

        current_round = init_round

    elapsed_seconds = int((time_now - current_round.round_start_time).total_seconds())
    remaining_time = max(0, current_round.phase_duration - elapsed_seconds)

    if remaining_time <= 0:
        if current_round.phase == PhaseStatus.BETTING:
            current_round.phase = PhaseStatus.SPINNING
            current_round.round_start_time = time_now
            current_round.phase_duration = 3
            await session.commit()
        elif current_round.phase == PhaseStatus.SPINNING:
            current_round.phase = PhaseStatus.RESULT
            current_round.round_start_time = time_now
            current_round.phase_duration = 5
            await session.commit()
        elif current_round.phase == PhaseStatus.RESULT:
            current_round.phase = PhaseStatus.BETTING
            current_round.round_start_time = time_now
            current_round.phase_duration = 5
            await session.commit()

    return {
        "created_at": current_round.created_at,
        "round_start_time": current_round.round_start_time,
        "phase": current_round.phase,
        "phase_duration": current_round.phase_duration,
    }


# stmt = insert(Roulette).values(phase=PhaseStatus.BETTING)
# await session.execute(stmt)
# await session.commit()
# sleep(2)
# stmt = insert(Roulette).values(phase=PhaseStatus.SPINNING)
# await session.execute(stmt)
# await session.commit()
# sleep(2)
# stmt = insert(Roulette).values(phase=PhaseStatus.RESULT)
# await session.execute(stmt)
# await session.commit()
