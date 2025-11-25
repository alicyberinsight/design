import json
from typing import Any

from aio_pika import Message, connect_robust
from aio_pika.abc import (
    AbstractRobustChannel,
    AbstractRobustConnection,
    DeliveryMode,
)

from src.app_config import AppConfig
from src.domain.client import IMessageBus
from src.domain.model import QueueTopic


class MessageBus(IMessageBus):
    def __init__(
        self,
        app_config: AppConfig,
    ) -> None:
        self._url = app_config.rabbitmq_url
        self._connection: AbstractRobustConnection | None = None
        self._channel: AbstractRobustChannel | None = None

    async def connect(self) -> None:
        await self.disconnect()

        self._connection = await connect_robust(self._url)
        self._channel = await self._connection.channel()

    async def disconnect(self) -> None:
        if self._connection:
            try:
                await self._connection.close()
            except:
                pass

        self._connection = None
        self._channel = None

    async def publish(
        self,
        queue: QueueTopic,
        message: dict[str, Any],
    ) -> None:
        if not self._channel or self._channel.is_closed:
            raise RuntimeError("MessageBus is not connected")

        body = json.dumps(message).encode()
        await self._channel.default_exchange.publish(
            Message(body=body, delivery_mode=DeliveryMode.PERSISTENT),
            routing_key=queue.value,
        )
