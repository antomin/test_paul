from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from config import settings


class DatabaseHelper:
    def __init__(
        self, url: str, echo: bool = False, echo_pool: bool = False, max_overflow: int = 10, pool_size: int = 5
    ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            max_overflow=max_overflow,
            pool_size=pool_size,
        )

        self.session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_maker() as session:
            yield session


db = DatabaseHelper(settings.database_url)
