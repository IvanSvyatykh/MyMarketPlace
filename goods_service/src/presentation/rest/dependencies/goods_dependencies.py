from typing import AsyncGenerator, Any

from sqlalchemy.ext.asyncio import AsyncSession

from goods_service.src.application.command.add_goods_category import AddGoodsCategoryCommand
from goods_service.src.domain.repositories.goods_repository import GoodsRepositoryInterface
from goods_service.src.domain.repositories.goods_category_repository import GoodsCategoryRepositoryInterface
from goods_service.src.domain.repositories.s3_repository import S3RepositoryInterface
from goods_service.src.infrastructure.db.repositories.goods_repository import SQLAlchemyGoodsRepository
from fastapi import Depends, Request
from goods_service.src.application.query.get_goods import GetGoodsQuery
from goods_service.src.application.command.add_good import AddGoodsCommand
from goods_service.src.infrastructure.db.repositories.goods_category_repository import SQLAlchemyGoodsCategoryRepository
from goods_service.src.infrastructure.s3.minio.minio_repository import S3MinioRepository


async def __get_session(request: Request) -> AsyncGenerator[AsyncSession, Any]:
    async with request.app.state.async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()


async def __get_goods_repository(session: AsyncSession = Depends(__get_session)) -> GoodsRepositoryInterface:
    return SQLAlchemyGoodsRepository(session)


async def __get_goods_category_repository(
        session: AsyncSession = Depends(__get_session)) -> GoodsCategoryRepositoryInterface:
    return SQLAlchemyGoodsCategoryRepository(session)


async def __get_photo_repository(request: Request) -> S3RepositoryInterface:
    return S3MinioRepository(request.app.state.minio_client)


async def get_goods_get_query(repository=Depends(__get_goods_repository)) -> GetGoodsQuery:
    return GetGoodsQuery(repository)


async def get_goods_add_command(goods_repository=Depends(__get_goods_repository),
                                goods_category_repository=Depends(__get_goods_category_repository)) -> AddGoodsCommand:
    return AddGoodsCommand(goods_repository, goods_category_repository)


async def get_goods_category_add_command(
        repository=Depends(__get_goods_category_repository)) -> AddGoodsCategoryCommand:
    return AddGoodsCategoryCommand(repository=repository)
