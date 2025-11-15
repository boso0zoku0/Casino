from fastapi import FastAPI
import uvicorn
from core.auth.views import router as auth_router
from core.roulette.views import router as roulette_router

origins = ["*"]
app = FastAPI()
app.include_router(auth_router)
app.include_router(roulette_router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
