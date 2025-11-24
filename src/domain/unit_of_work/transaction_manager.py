from contextlib import AbstractAsyncContextManager
from typing import Protocol

from src.domain.unit_of_work import IUnitOfWork


class ITransactionManager(Protocol):
    def get_uow(self) -> AbstractAsyncContextManager[IUnitOfWork]:
        pass
