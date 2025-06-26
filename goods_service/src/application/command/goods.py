import uuid

from goods_service.src.domain.repositories.goods_repository import GoodsRepositoryInterface
from goods_service.src.presentation.rest.schemas.goods import AddGoodRequest, AddGoodsResponse
from goods_service.src.domain.dto.goods import AddGoodRequestDTO
from goods_service.src.domain.enteties.good import Good
from goods_service.src.domain.repositories.goods_category_repository import GoodsCategoryRepositoryInterface
from goods_service.src.domain.exceptions.goods_exceptions import CategoryNotFound
from goods_service.src.domain.repositories.s3_repository import S3RepositoryInterface


class AddGoodsCommand:

    def __init__(self, goods_repository: GoodsRepositoryInterface,
                 goods_category_repository: GoodsCategoryRepositoryInterface):
        self.__goods_repository = goods_repository
        self.__goods_category_repository = goods_category_repository

    async def execute(self, goods_request: AddGoodRequestDTO) -> uuid.UUID:
        try:
            category = await self.__goods_category_repository.get_category_by_name(goods_request.category_name)
            if category is None:
                raise CategoryNotFound("Category with this name doesn't exist !")
            good = Good(id=None, category_id=category.id, price=goods_request.price,
                        amount=goods_request.amount, name=goods_request.name)
            await  self.__goods_repository.add_good(good)
        except Exception as e:
            raise e

        return good.id


class AddGoodsPhotoCommand:
    def __init__(self, goods_repository: GoodsRepositoryInterface, s3_repository: S3RepositoryInterface):
        self.__goods_repository = goods_repository
        self.__s3_repository = s3_repository

    async def execute(self) -> None:
        pass
