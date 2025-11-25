from src.domain.client import IMessageBus
from src.domain.model import QueueTopic


class JobGateway:
    def __init__(
        self,
        message_bus: IMessageBus,
    ) -> None:
        self._message_bus = message_bus

    async def index_blog(
        self,
        blog_id: int,
    ) -> None:
        await self._message_bus.publish(
            queue=QueueTopic.INDEX_BLOG,
            message={"blog_id": blog_id},
        )
