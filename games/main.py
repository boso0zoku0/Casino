import asyncio
import logging
from typing import List

from fastapi import FastAPI, Depends
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocketDisconnect, WebSocket

from core.auth.views import router as auth_router
from core.config import settings
from core.roulette.views import router as roulette_router

from payments import router as payment_router
import aio_pika

origins = ["*"]
app = FastAPI()

app.include_router(payment_router)
app.include_router(auth_router)
app.include_router(roulette_router)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:5173",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(
    format=settings.logging.log_format,
    level=settings.logging.log_level_name,
    datefmt=settings.logging.date_format,
)


@app.get("/")
async def hello(name: str):
    return {"Hello": {name}}


# Ваш менеджер подключений
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


# Создаем соединение с RabbitMQ
async def connect_to_rabbit():
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    return connection


# Функция для обработки сообщений из RabbitMQ и отправки клиентам
async def consume_messages():
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost:5672/")
    channel = await connection.channel()
    queue = await channel.declare_queue("chat_queue", durable=True)
    async for message in queue:
        async with message.process():
            await manager.broadcast(message.body.decode())


# Обработчик WebSocket
@app.websocket("/ws/chat/")
async def chat_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    # Запускаем задачу прослушивания RabbitMQ при подключении клиента
    consumer_task = asyncio.create_task(consume_messages())
    try:
        async with await aio_pika.connect_robust(
            "amqp://guest:guest@localhost/"
        ) as connection:
            channel = await connection.channel()
            await channel.default_exchange.publish(
                aio_pika.Message(body=f"New connection established".encode()),
                routing_key="chat_system",
            )
        while True:
            data = await websocket.receive_text()
            # Отправляем сообщение в очередь RabbitMQ
            connection = await connect_to_rabbit()
            channel = await connection.channel()
            await channel.default_exchange.publish(
                aio_pika.Message(body=data.encode()), routing_key="chat_queue"
            )
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        consumer_task.cancel()


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
