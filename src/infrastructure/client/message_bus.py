from typing import Any

from src.app_config import AppConfig
from src.domain.client import IMessageBus
from src.domain.model import QueueTopic


class MessageBus(IMessageBus):
    def __init__(
        self,
        app_config: AppConfig,
    ) -> None:
        self._app_config = app_config

    async def connect(self) -> None:
        raise NotImplementedError()

    async def disconnect(self) -> None:
        raise NotImplementedError()

    async def publish(
        self,
        queue: QueueTopic,
        message: dict[str, Any],
    ) -> None:
        raise NotImplementedError()
