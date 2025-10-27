from pathlib import Path

from pydantic_settings import BaseSettings
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent.parent


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "core" / "auth" / "private_key.pem"
    public_key_path: Path = BASE_DIR / "core" / "auth" / "public_key.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 3
    refresh_token_expire_days: int = 30


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    auth: str = "/auth"


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = "postgresql+asyncpg://postgres:matvei225CC@:5432/casino"
    db_echo: bool = True
    # access_token: AccessToken = AccessToken()
    auth_jwt: AuthJWT = AuthJWT()


settings = Setting()
