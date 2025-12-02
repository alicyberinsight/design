from pydantic import BaseModel
from src.app_config import AppConfig
from enum import StrEnum

from faststream.rabbit import RabbitBroker, RabbitQueue


class QueueTopic(StrEnum):
    INDEX_BLOG = "index_blog"


class MessageBus:
    def __init__(
        self,
        app_config: AppConfig,
    ) -> None:
        self._broker = RabbitBroker(app_config.rabbitmq_url)

    async def connect(self) -> None:
        await self._broker.connect()

    async def disconnect(self) -> None:
        await self._broker.stop()

    async def publish(
        self,
        topic: QueueTopic,
        message: BaseModel,
    ) -> None:
        await self._broker.publish(
            message,
            queue=RabbitQueue(
                name=topic.value,
                durable=True,
                auto_delete=False,
            ),
            persist=True,
        )
