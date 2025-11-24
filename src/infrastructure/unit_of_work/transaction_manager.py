from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.domain.unit_of_work import ITransactionManager
from .unit_of_work import UnitOfWork


class TransactionManager(ITransactionManager):
    def __init__(self) -> None:
        engine = create_async_engine(
            "",
            echo=True,
            future=True,
            pool_size=10,
            max_overflow=20,
            pool_timeout=30,
        )
        self._async_session_factory = async_sessionmaker(
            bind=engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )

    async def get_uow(self) -> AsyncIterator[UnitOfWork]:
        async with self._async_session_factory() as session:
            try:
                yield UnitOfWork(session=session)
            except Exception as e:
                await session.rollback()

                raise e
