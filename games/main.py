from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from core.auth.views import router as auth_router
from core.roulette.views import router as roulette_router

origins = ["*"]
app = FastAPI()
app.include_router(auth_router)
app.include_router(roulette_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def hello(name: str):
    return {"Hello": {name}}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
