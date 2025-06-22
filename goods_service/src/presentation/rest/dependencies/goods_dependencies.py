from sqlalchemy.ext.asyncio import AsyncSession

from goods_service.src.application.command.goods_category import AddGoodsCategoryCommand
from goods_service.src.infrastructure.db.session_factory import get_session
from goods_service.src.domain.repositories.goods_repository import GoodsRepositoryInterface
from goods_service.src.domain.repositories.goods_category_repository import GoodsCategoryRepositoryInterface
from goods_service.src.infrastructure.db.repositories.goods_repository import SQLAlchemyGoodsRepository
from fastapi import Depends
from goods_service.src.application.query.goods import GetGoodsQuery
from goods_service.src.application.command.goods import AddGoodsCommand
from goods_service.src.infrastructure.db.repositories.goods_category_repository import SQLAlchemyGoodsCategoryRepository


async def __get_goods_repository(session: AsyncSession = Depends(get_session)) -> GoodsRepositoryInterface:
    return SQLAlchemyGoodsRepository(session)


async def __get_goods_category_repository(
        session: AsyncSession = Depends(get_session)) -> GoodsCategoryRepositoryInterface:
    return SQLAlchemyGoodsCategoryRepository(session)


async def get_goods_get_query(repository=Depends(__get_goods_repository)) -> GetGoodsQuery:
    return GetGoodsQuery(repository)


async def get_goods_add_command(goods_repository=Depends(__get_goods_repository),
                                goods_category_repository=Depends(__get_goods_category_repository)) -> AddGoodsCommand:
    return AddGoodsCommand(goods_repository, goods_category_repository)


async def get_goods_category_add_command(
        repository=Depends(__get_goods_category_repository)) -> AddGoodsCategoryCommand:
    return AddGoodsCategoryCommand(repository=repository)
