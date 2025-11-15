import datetime
from datetime import timedelta, time, datetime
from time import timezone

import bcrypt
import jwt
from pydantic import BaseModel
from sqlalchemy.util import await_only

from core.config import settings
from core.models import Players


class AuthJWT:
    def encode_jwt(
        self,
        payload: dict,
        expire_minutes_access: int = settings.auth_jwt.access_token_expire_minutes,
        expire_minutes_refresh: int = settings.auth_jwt.refresh_token_expire_days,
        private_key: str = settings.auth_jwt.private_key_path.read_text(),
        algorithm: str = settings.auth_jwt.algorithm,
        is_refresh: bool = False,
    ) -> str:
        to_encode = payload.copy()
        now = datetime.now()
        if is_refresh:
            expire = now + timedelta(minutes=expire_minutes_refresh)
        else:
            expire = now + timedelta(minutes=expire_minutes_access)
        to_encode.update(exp=expire, iat=now)
        return jwt.encode(payload=to_encode, key=private_key, algorithm=algorithm)

    @staticmethod
    def decode_jwt(
        token: str | bytes,
        public_key: str = settings.auth_jwt.public_key_path.read_text(),
        algorithm: str = settings.auth_jwt.algorithm,
    ) -> None:
        return jwt.decode(
            token=token,
            key=public_key,
            algorithms=[algorithm],
        )

    @staticmethod
    def hash_password(password: str) -> bytes:
        salt = bcrypt.gensalt()
        pwd_bytes = password.encode("utf-8")
        return bcrypt.hashpw(pwd_bytes, salt)

    def validate_password(
        password: str,
        hashed_password: bytes,
    ) -> bool:
        return bcrypt.checkpw(
            password=password.encode(),
            hashed_password=hashed_password,
        )


helper_jwt = AuthJWT()
