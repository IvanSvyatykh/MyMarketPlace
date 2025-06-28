from goods_service.src.domain.repositories.goods_repository import GoodsRepositoryInterface
from goods_service.src.application.dto.goods import GetGoodsRequestDTO, GetGoodsResponseDTO


class GetGoodsQuery:

    def __init__(self, repository: GoodsRepositoryInterface):
        self.repository = repository

    async def execute(self, goods_query: GetGoodsRequestDTO) -> list[GetGoodsResponseDTO]:
        goods = await  self.repository.get_goods(offset=goods_query.offset, limit=goods_query.limit)
        return [GetGoodsResponseDTO(id=good.id, category_name=good.category_name, name=good.name, amount=good.amount,
                                    price=good.price) for good in goods]
