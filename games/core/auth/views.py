from OpenSSL.rand import status
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from pydantic import BaseModel
from fastapi.security import (
    HTTPBearer,
    OAuth2PasswordBearer,
    HTTPAuthorizationCredentials,
)
from fastapi import Form, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.sql.annotation import Annotated

from core.auth.helper import helper_jwt
from core.models import Players
from core.models.tokens import TokenInfo
from core.schemas import PlayersGet, PlayersPost

oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/token")

router = APIRouter(prefix="/auth", tags=["AuthJWT"])


# def validate_auth_user(session: AsyncSession, username: Form, password: Form):
#     get_db_players = select(Players).where(Players.username == username)
#     session.get(Players, username)
#     if not get_db_players:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="User not found"
#         )
#     check_password = helper_jwt.validate_password(
#         password=password, hash_password=get_db_players
#     )
#     if not check_password:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="User not found"
#         )
#     return get_db_players


def validate_and_take_user(
    session: AsyncSession,
    username: Annotated[HTTPAuthorizationCredentials, Depends(oauth2)],
    password: Annotated[HTTPAuthorizationCredentials, Depends(oauth2)],
):
    get_db_players = select(Players).where(Players.username == username)
    session.get(Players, username)
    if not get_db_players:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User not found"
        )
    check_password = helper_jwt.validate_password(
        password=password, hash_password=get_db_players
    )
    if not check_password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User not found"
        )
    return get_db_players


@router.post("/login", response_model=None)
def login_user(player: PlayersPost):
    access_token = helper_jwt.create_access_token(player=player)
    refresh_token = helper_jwt.create_refresh_token(player=player)
    return TokenInfo(
        access_token=access_token, refresh_token=refresh_token, token_type="Bearer"
    )


@router.post("/token")
def generate_token(player: PlayersPost):
    return helper_jwt.create_access_token(player=player)


#
# @router.post('/login', response_model=status.HTTP_201_CREATED)
# def log_in(player: Players, session: AsyncSession = Depends(validate_auth_user)):
#     pass
