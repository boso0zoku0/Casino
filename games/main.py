from fastapi import FastAPI
from views import router as games_router
from core.views.players import router as players_router
from core.auth.views import router as auth_router

app = FastAPI()
app.include_router(games_router)
app.include_router(players_router)
app.include_router(auth_router)
