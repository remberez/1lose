from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from core.config import settings


class DataBaseHelper:
    # Вспомогательный класс для работы с базой данных.

    def __init__(
        self,
        url: str,
        echo: bool = False,
        echo_pool: bool = False,
        max_overflow: int = 10,
        pool_size: int = 5,
    ):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            max_overflow=max_overflow,
            pool_size=pool_size,
        )
        self.session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )
        self._session = None

    async def dispose(self):
        # Освобождение пула соединений.
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        if self._session is None:
            self._session = self.session_maker()
        async with self._session as session:
            yield session

    async def reset_session(self):
        if self._session:
            await self._session.close()
            self._session = None


db_helper = DataBaseHelper(
    url=str(settings.database.url),
    echo_pool=settings.database.echo_pool,
    echo=settings.database.echo,
    pool_size=settings.database.pool_size,
    max_overflow=settings.database.max_overflow,
)
