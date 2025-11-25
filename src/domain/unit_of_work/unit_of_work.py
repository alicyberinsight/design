from typing import Protocol

from src.domain.repository import (
    IBlogRepository,
    IUserRepository,
)


class IUnitOfWork(Protocol):
    async def commit(self) -> None:
        pass

    async def rollback(self) -> None:
        pass

    @property
    def blog_repository(self) -> IBlogRepository:
        pass

    @property
    def user_repository(self) -> IUserRepository:
        pass
