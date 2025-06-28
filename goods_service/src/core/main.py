from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from miniopy_async import Minio

from goods_service.src.presentation.rest.v1.goods import goods_router
from config import PORT
from goods_service.src.domain.exceptions.goods_exceptions import DomainException
from goods_service.src.presentation.rest.error_handlers.goods_handlers import domain_error_handler
from goods_service.src.core.config import (MINIO_HOST, MINIO_SECRET_KEY, MINIO_ACCESS_KEY, MINIO_API_PORT, USE_HTTPS)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from goods_service.src.presentation.rest.middleware.file_middleware import file_validation_middleware
from goods_service.src.core.config import DATABASE_URL


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.minio_client = Minio(endpoint=f"{MINIO_HOST}:{MINIO_API_PORT}",
                                   access_key=MINIO_ACCESS_KEY,
                                   secret_key=MINIO_SECRET_KEY,
                                   secure=USE_HTTPS)

    engine = create_async_engine(DATABASE_URL, pool_size=10,
                                 max_overflow=20, )

    app.state.async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

    yield
    await app.state.minio_client.close_session()


app = FastAPI(lifespan=lifespan)

app.include_router(goods_router)
app.middleware("http")(file_validation_middleware)
app.exception_handler(DomainException)(domain_error_handler)
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=PORT)
