from catalog_service.src.presentation.rest.schemas.goods import GetGoodsRequest
from catalog_service.src.domain.repositories.goods_repository import GoodsRepositoryInterface
from catalog_service.src.presentation.rest.schemas.goods import GetGoodsResponse


class GetGoodsQuery:

    def __init__(self, repository: GoodsRepositoryInterface):
        self.repository = repository

    async def execute(self, goods_request: GetGoodsRequest) -> list[GetGoodsResponse]:
        goods = await  self.repository.get_goods(offset=goods_request.offset, limit=goods_request.limit)
        return [GetGoodsResponse(id=good.id, name=good.name, category_name=good.category_name, photo_url=good.photo_url,
                                 amount=good.amount, price=good.price) for good in goods
                for good in goods]
