from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.model import User
from src.domain.repository import IUserRepository
from src.infrastructure.table import UserTable


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_user(self, email: str, full_name: str) -> User:
        user = UserTable(
            email=email,
            full_name=full_name,
        )
        self._session.add(user)
        await self._session.flush()
        await self._session.refresh(user)
        return User(
            id=user.id,
            email=user.email,
            full_name=user.full_name,
        )
