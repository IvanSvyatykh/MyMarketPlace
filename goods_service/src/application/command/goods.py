from goods_service.src.domain.repositories.goods_repository import GoodsRepositoryInterface
from goods_service.src.presentation.rest.schemas.goods import AddGoodRequest
from goods_service.src.domain.enteties.good import Good
from goods_service.src.domain.repositories.goods_category_repository import GoodsCategoryRepositoryInterface
from goods_service.src.domain.exceptions.goods_exceptions import CategoryNotFound


class AddGoodsCommand:

    def __init__(self, goods_repository: GoodsRepositoryInterface,
                 goods_category_repository: GoodsCategoryRepositoryInterface):
        self.__goods_repository = goods_repository
        self.__goods_category_repository = goods_category_repository

    async def execute(self, goods_request: AddGoodRequest) -> None:
        try:
            category = await self.__goods_category_repository.get_category_by_name(goods_request.category_name)
            if category is None:
                raise CategoryNotFound("Category with this name doesn't exist !")
            await  self.__goods_repository.add_good(
                Good(id=None, category_id=category.id, price=goods_request.price,
                     amount=goods_request.amount, photo_url=None, name=goods_request.name))
        except Exception as e:
            raise e
