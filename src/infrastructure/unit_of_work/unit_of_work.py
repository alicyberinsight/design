from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.repository import IBlogRepository
from src.domain.repository import IUserRepository
from src.domain.unit_of_work import IUnitOfWork
from src.infrastructure.repository import BlogRepository
from src.infrastructure.repository import UserRepository


class UnitOfWork(IUnitOfWork):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

        self._blog_repository: IBlogRepository | None = None
        self._user_repository: IUserRepository | None = None

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

    @property
    def blog_repository(self) -> IBlogRepository:
        if self._blog_repository is None:
            self._blog_repository = BlogRepository(session=self._session)

        return self._blog_repository

    @property
    def user_repository(self) -> IUserRepository:
        if self._user_repository is None:
            self._user_repository = UserRepository(session=self._session)

        return self._user_repository
