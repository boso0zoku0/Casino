from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class PlayersGet(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    password: str
    balance: int | None = 0
    email: EmailStr | None = None
    years_active: int | None = 0
    cookies: str | None = None
    access_token: str | None = None
    created_at: datetime

    def __str__(self):
        return f"Player(id={self.id}, username={self.username}, password='{self.password}', balance='{self.balance}' email='{self.email}')"


class PlayersPost(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str
    password: str
    email: EmailStr | None = None

    def __str__(self):
        return f"Player(username={self.username}, password='{self.password}', balance='{self.balance}' email='{self.email}')"
