import uuid

from sqlalchemy.exc import IntegrityError

from goods_service.src.domain.repositories.goods_category_repository import GoodsCategoryRepositoryInterface
from goods_service.src.domain.enteties.goods_category import GoodCategory
from goods_service.src.domain.exceptions.goods_exceptions import CategoryAlreadyExists


class AddGoodsCategoryCommand:

    def __init__(self, repository: GoodsCategoryRepositoryInterface):
        self.repository = repository

    async def execute(self, category_name: str) -> uuid.UUID:
        try:
            res = await self.repository.add_category(GoodCategory(id=None, name=category_name))
        except IntegrityError as e:
            if "good_category_name_key" in str(e):
                raise CategoryAlreadyExists("Category already exists !")
        return res.id
