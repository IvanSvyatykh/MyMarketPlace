from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from catalog_service.src.core.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, pool_size=10,
                             max_overflow=20, )

session_factory = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncSession:
    async with session_factory() as session:
        try:
            yield session
        finally:
            await session.close()
