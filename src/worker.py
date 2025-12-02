import asyncio
from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitQueue

from src.app_config import AppConfig
from src.message_bus import QueueTopic
from src.main import TaskI

broker = RabbitBroker(AppConfig().rabbitmq_url)
app = FastStream(broker)


@broker.subscriber(
    RabbitQueue(
        name=QueueTopic.INDEX_BLOG.value,
        durable=True,
        auto_delete=False,
    )
)
async def worker_handler(msg: TaskI) -> None:
    print(f"Processing task: {msg.id} - {msg.name}")
    await asyncio.sleep(12)
    print(f"Completed task: {msg.id} - {msg.name}")
