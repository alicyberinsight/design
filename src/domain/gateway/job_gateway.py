from src.domain.client import IRabbitMQClient
from src.domain.model.job_queue import QueueTopic


class JobGateway:
    def __init__(
        self,
        rabbitmq_client: IRabbitMQClient,
    ) -> None:
        self._rabbitmq_client = rabbitmq_client

    async def index_blog(
        self,
        blog_id: int,
    ) -> None:
        await self._rabbitmq_client.publish(
            queue=QueueTopic.INDEX_BLOG,
            message={"blog_id": blog_id},
        )
