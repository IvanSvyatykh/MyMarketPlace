from sqlalchemy.ext.asyncio import AsyncSession
from catalog_service.src.infrastructure.db.session_factory import get_session
from catalog_service.src.domain.repositories.goods_repository import GoodsRepositoryInterface
from catalog_service.src.infrastructure.db.repositories.goods_repository import SQLAlchemyGoodsRepository
from fastapi import Depends
from catalog_service.src.application.query.goods import GetGoodsQuery


async def __get_goods_repository(session: AsyncSession = Depends(get_session)) -> GoodsRepositoryInterface:
    return SQLAlchemyGoodsRepository(session)


async def get_goods_get_query(repository=Depends(__get_goods_repository)) -> GetGoodsQuery:
    return GetGoodsQuery(repository)
