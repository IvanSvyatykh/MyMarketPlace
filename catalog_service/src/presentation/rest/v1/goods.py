from fastapi import APIRouter
from fastapi.params import Depends

from catalog_service.src.application.query.goods import GetGoodsQuery
from ..schemas.goods import GoodsResponse, GoodsRequest
from catalog_service.src.presentation.rest.dependencies.goods_dependencies import get_goods_get_query

goods_router = APIRouter(prefix="/goods/v1")


@goods_router.get("/", response_model=list[GoodsResponse])
async def get_goods(goods_query: GetGoodsQuery = Depends(get_goods_get_query), offset: int = 0, limit: int = 10) -> \
        list[GoodsResponse]:
    return await goods_query.execute(GoodsRequest(offset=offset, limit=limit))
