from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete
from goods_service.src.domain.enteties.good import Good
from goods_service.src.domain.agregates.good import Good as GoodAggregate
from ..models.model import GoodsModel, GoodCategoryModel
from goods_service.src.domain.repositories.goods_repository import GoodsRepositoryInterface


class SQLAlchemyGoodsRepository(GoodsRepositoryInterface):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_goods(self, offset: int, limit: int) -> list[GoodAggregate]:
        res = await  (self._session
        .execute(
            select(GoodsModel.id, GoodCategoryModel.name.label("category_name"), GoodsModel.name,
                   GoodsModel.price,
                   GoodsModel.amount)
            .join(GoodCategoryModel, GoodsModel.category_id == GoodCategoryModel.id)
            .limit(limit)
            .offset(offset)))
        res = res.all()
        return [GoodAggregate(*row) for row in res]

    async def add_good(self, good: Good) -> None:
        try:
            await self._session.execute(
                insert(GoodsModel).values(id=good.id, category_id=good.category_id, name=good.name,
                                          price=good.price,
                                          amount=good.amount))
            await self._session.commit()
        except Exception as e:
            await self._session.rollback()
            raise e
