from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from src.domain.gateway import JobGateway
from src.domain.service import (
    BlogService,
    UserService,
)
from src.infrastructure.client import MessageBus
from src.infrastructure.unit_of_work import TransactionManager

from .app_config import AppConfig


class AppContainer(DeclarativeContainer):
    app_config = providers.Singleton(AppConfig)

    transaction_manager = providers.Singleton(
        TransactionManager,
        app_config=app_config,
    )

    message_bus = providers.Singleton(
        MessageBus,
        app_config=app_config,
    )

    job_gateway = providers.Singleton(
        JobGateway,
        message_bus=message_bus,
    )

    blog_service = providers.Factory(
        BlogService,
        transaction_manager=transaction_manager,
        job_gateway=job_gateway,
    )

    user_service = providers.Factory(
        UserService,
        transaction_manager=transaction_manager,
    )
