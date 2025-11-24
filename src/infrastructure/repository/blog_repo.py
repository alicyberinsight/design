from sqlalchemy.ext.asyncio import AsyncSession


from src.domain.model import Blog
from src.domain.repository import IBlogRepository
from src.infrastructure.table import BlogTable


class BlogRepository(IBlogRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_blog(self, title: str, content: str) -> Blog:
        blog = BlogTable(title=title, content=content)
        self._session.add(blog)
        await self._session.flush()
        await self._session.refresh(blog)
        return Blog(
            id=blog.id,
            title=blog.title,
            content=blog.content,
        )
