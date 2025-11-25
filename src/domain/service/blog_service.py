from src.domain.gateway import JobGateway
from src.domain.model import (
    Blog,
    CreateBlogRequest,
)
from src.domain.unit_of_work import ITransactionManager


class BlogService:
    def __init__(
        self,
        transaction_manager: ITransactionManager,
        job_gateway: JobGateway,
    ) -> None:
        self._transaction_manager = transaction_manager
        self._job_gateway = job_gateway

    async def create_blog_post(
        self,
        create_blog_request: CreateBlogRequest,
    ) -> Blog:
        async with self._transaction_manager.get_uow() as uow:
            blog = await uow.blog_repository.create_blog(
                title=create_blog_request.title,
                content=create_blog_request.content,
            )
            await self._job_gateway.index_blog(blog_id=blog.id)
            await uow.commit()
            return blog
