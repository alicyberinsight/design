from typing import (
    Any,
    Protocol,
)

from src.domain.model import QueueTopic


class IMessageBus(Protocol):

    async def connect(self) -> None:
        pass

    async def disconnect(self) -> None:
        pass

    async def publish(
        self,
        queue: QueueTopic,
        message: dict[str, Any],
    ) -> None:
        pass
