from src.model import (
    Blog,
    CreateBlogRequest,
)
from src.unit_of_work import TransactionManager


class BlogService:
    def __init__(
        self,
        transaction_manager: TransactionManager,
    ) -> None:
        self._transaction_manager = transaction_manager

    async def create_blog_post(
        self,
        create_blog_request: CreateBlogRequest,
    ) -> Blog:
        async with self._transaction_manager.get_uow() as uow:
            blog = await uow.blog_repository.create_blog(
                title=create_blog_request.title,
                content=create_blog_request.content,
            )
            await uow.commit()
            return blog
