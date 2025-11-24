from typing import Protocol

from src.domain.model import User


class IUserRepository(Protocol):
    async def create_user(self, email: str, full_name: str) -> User:
        pass
