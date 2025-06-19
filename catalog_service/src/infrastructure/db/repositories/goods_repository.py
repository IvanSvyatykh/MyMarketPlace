from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from catalog_service.src.domain.agregates.good import Good
from ..models.model import GoodsModel, GoodCategoryModel
from catalog_service.src.domain.repositories.goods_repository import GoodsRepositoryInterface


class SQLAlchemyGoodsRepository(GoodsRepositoryInterface):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_goods(self, offset: int, limit: int) -> list[Good]:
        res = await  (self._session
        .execute(
            select(GoodsModel.id, GoodCategoryModel.name.label("category_name"), GoodsModel.name, GoodsModel.photo_url,
                   GoodsModel.price,
                   GoodsModel.amount)
            .join(GoodCategoryModel, GoodsModel.category_id == GoodCategoryModel.id)
            .limit(limit)
            .offset(offset)))
        res = res.all()
        return [Good(*row) for row in res]
