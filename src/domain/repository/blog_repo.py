from typing import Protocol

from src.domain.model import Blog


class IBlogRepository(Protocol):
    async def create_blog(self, title: str, content: str) -> Blog:
        pass
