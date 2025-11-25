from src.model import (
    CreateUserRequest,
    User,
)
from src.unit_of_work import TransactionManager


class UserService:
    def __init__(
        self,
        transaction_manager: TransactionManager,
    ) -> None:
        self._transaction_manager = transaction_manager

    async def create_user(
        self,
        createUserRequest: CreateUserRequest,
    ) -> User:
        async with self._transaction_manager.get_uow() as uow:
            user = await uow.user_repository.create_user(
                email=createUserRequest.email,
                full_name=createUserRequest.full_name,
            )
            await uow.commit()
            return user
