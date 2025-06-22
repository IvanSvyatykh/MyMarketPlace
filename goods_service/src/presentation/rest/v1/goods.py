from http.client import responses

from fastapi import APIRouter, Query, Response, Request, HTTPException
from fastapi.params import Depends
from goods_service.src.application.command.goods_category import AddGoodsCategoryCommand
from goods_service.src.application.query.goods import GetGoodsQuery
from ..schemas.goods import GetGoodsResponse, GetGoodsRequest, AddGoodRequest
from ..schemas.goods_category import AddGoodsCategoryRequest, AddGoodsCategoryResponse
from goods_service.src.presentation.rest.dependencies.goods_dependencies import get_goods_get_query, \
    get_goods_add_command, get_goods_category_add_command
from goods_service.src.application.command.goods import AddGoodsCommand

goods_router = APIRouter(prefix="/goods/v1")


@goods_router.get("/", response_model=list[GetGoodsResponse], status_code=200)
async def get_goods(goods_query: GetGoodsQuery = Depends(get_goods_get_query),
                    offset: int = Query(default=0, ge=0),
                    limit: int = Query(default=10, ge=0)) -> list[GetGoodsResponse]:
    return await goods_query.execute(GetGoodsRequest(offset=offset, limit=limit))


@goods_router.post("/", status_code=201)
async def add_goods(request: AddGoodRequest, goods_command: AddGoodsCommand = Depends(get_goods_add_command)) -> None:
    await goods_command.execute(request)


@goods_router.post("/category", status_code=201, response_model=AddGoodsCategoryResponse)
async def add_category(request: AddGoodsCategoryRequest,
                       goods_category_command: AddGoodsCategoryCommand = Depends(
                           get_goods_category_add_command)) -> AddGoodsCategoryResponse:
    return await goods_category_command.execute(request)
