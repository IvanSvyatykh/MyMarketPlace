from sqlalchemy.ext.asyncio import AsyncSession

from catalog_service.src.domain.enteties.goods_category import GoodCategory
from catalog_service.src.domain.repositories.goods_category_repository import GoodsCategoryRepositoryInterface
from sqlalchemy import select
from ..models.model import GoodCategoryModel


class SQLAlchemyGoodsCategoryRepository(GoodsCategoryRepositoryInterface):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_category_by_name(self, name: str) -> GoodCategory | None:
        res = await  self._session.execute(select(GoodCategoryModel).where(GoodCategoryModel.name == name))
        res = res.scalar_one_or_none()
        return GoodCategory(id=res.id, name=res.name) if res else None
