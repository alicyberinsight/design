from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.model import User
from src.domain.repository import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_user(self, email: str, full_name: str) -> User:
        raise NotImplementedError("Method not implemented yet.")
