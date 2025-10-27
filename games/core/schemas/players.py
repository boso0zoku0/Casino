from pydantic import BaseModel, ConfigDict, EmailStr


class PlayersGet(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    password: str
    balance: int
    email: EmailStr
    years_active: int

    def __str__(self):
        return f"Player(id={self.id}, username={self.username}, password='{self.password}', balance='{self.balance}' email='{self.email}')"


class PlayersPost(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str
    password: str
    balance: int
    email: EmailStr
    years_active: int

    def __str__(self):
        return f"Player(username={self.username}, password='{self.password}', balance='{self.balance}' email='{self.email}')"
