from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from goods_service.src.domain.enteties.good_category import GoodCategory
from goods_service.src.domain.repositories.goods_category_repository import GoodsCategoryRepositoryInterface
from sqlalchemy import select, insert, update, delete
from ..models.model import GoodCategoryModel


class SQLAlchemyGoodsCategoryRepository(GoodsCategoryRepositoryInterface):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_category_by_name(self, name: str) -> GoodCategory | None:
        res = await  self._session.execute(select(GoodCategoryModel).where(GoodCategoryModel.name == name))
        res = res.scalar_one_or_none()
        return GoodCategory(id=res.id, name=res.name) if res else None

    async def add_category(self, category: GoodCategory) -> GoodCategory:
        try:
            await self._session.execute(insert(GoodCategoryModel).values(id=category.id, name=category.name))
            await self._session.commit()
        except IntegrityError as e:
            await self._session.rollback()
            raise e
        return category
