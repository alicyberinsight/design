from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.app_config import AppConfig
from src.message_bus import MessageBus, QueueTopic


class TaskI(BaseModel):
    id: str
    name: str


message_bus = MessageBus(
    app_config=AppConfig(),
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await message_bus.connect()
    yield
    await message_bus.disconnect()


app = FastAPI(title="API", lifespan=lifespan)


@app.post("/start/${id}", status_code=202)
async def submit_task(id: str) -> TaskI:
    task = TaskI(id=id, name="Sample Task")
    try:
        await message_bus.publish(
            topic=QueueTopic.INDEX_BLOG,
            message=task,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return task
