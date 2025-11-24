from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.model import Blog
from src.domain.repository import IBlogRepository


class BlogRepository(IBlogRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_blog(self, title: str, content: str) -> Blog:
        raise NotImplementedError("Method not implemented yet.")
