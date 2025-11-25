from sqlalchemy.ext.asyncio import AsyncSession

from src.repository import (
    BlogRepository,
    UserRepository,
)


class UnitOfWork:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

        self._blog_repository: BlogRepository | None = None
        self._user_repository: UserRepository | None = None

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

    @property
    def blog_repository(self) -> BlogRepository:
        if self._blog_repository is None:
            self._blog_repository = BlogRepository(session=self._session)

        return self._blog_repository

    @property
    def user_repository(self) -> UserRepository:
        if self._user_repository is None:
            self._user_repository = UserRepository(session=self._session)

        return self._user_repository
