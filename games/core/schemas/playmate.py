from pydantic import BaseModel, ConfigDict, EmailStr


class PlaymateGet(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    bet: int

    def __str__(self):
        return f"Player(id={self.id}, username='{self.username}', bet='{self.bet}')"


class PlaymatePost(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str
    bet: int

    def __str__(self):
        return f"Player(id={self.id}, username='{self.username}', bet='{self.bet}')"
