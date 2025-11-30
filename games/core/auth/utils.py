import secrets
from typing import Annotated

from fastapi import Form, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from pydantic import BaseModel, EmailStr
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from core.auth import helper_jwt
from core.models import db_helper, Players
from core.schemas import PlayersPost

oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")


class SessionJwtTokens(BaseModel):
    session_id: str
    access_token: str
    token_type: str | None = None


async def entry_user(
    player: PlayersPost, session: AsyncSession = Depends(db_helper.session_dependency)
):
    add_user = Players(**player.model_dump())
    session.add(add_user)
    await session.commit()
    return {"Login": "success"}


async def validate_auth_user(
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
    username: str = Form(),
    password: str = Form(),
):
    stmt = select(Players).where(
        and_(Players.username == username, Players.password == password)
    )
    result = await session.execute(stmt)
    player = result.scalar()
    if player is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    return player


async def get_current_token_payload(
    token: str = Depends(oauth2),
) -> dict:
    try:
        payload = helper_jwt.decode_jwt(
            token=token,
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token error",
        )
    return payload


def generate_user_token() -> str:
    return secrets.token_urlsafe()
