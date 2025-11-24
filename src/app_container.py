from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from src.domain.service import (
    BlogService,
    UserService,
)
from src.infrastructure.unit_of_work import TransactionManager


class AppContainer(DeclarativeContainer):
    transaction_manager = providers.Singleton(TransactionManager)

    blog_service = providers.Factory(
        BlogService,
        transaction_manager=transaction_manager,
    )

    user_service = providers.Factory(
        UserService,
        transaction_manager=transaction_manager,
    )
