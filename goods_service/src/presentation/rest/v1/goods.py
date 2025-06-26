import uuid

from fastapi import APIRouter, Query, UploadFile, File, status
from fastapi.params import Depends
from goods_service.src.application.command.goods_category import AddGoodsCategoryCommand
from goods_service.src.application.query.goods import GetGoodsQuery
from ..schemas.goods import GetGoodsResponse, GetGoodsRequest, AddGoodRequest, AddGoodsResponse
from ..schemas.goods_category import AddGoodsCategoryRequest, AddGoodsCategoryResponse
from goods_service.src.presentation.rest.dependencies.goods_dependencies import get_goods_get_query, \
    get_goods_add_command, get_goods_category_add_command
from goods_service.src.application.command.goods import AddGoodsCommand
from goods_service.src.domain.enteties.photo import Photo
from goods_service.src.domain.dto.goods import GetGoodsRequestDTO, AddGoodRequestDTO

goods_router = APIRouter(prefix="/goods/v1")


@goods_router.get("/goods", response_model=list[GetGoodsResponse], status_code=status.HTTP_200_OK)
async def get_goods(goods_query: GetGoodsQuery = Depends(get_goods_get_query),
                    offset: int = Query(default=0, ge=0),
                    limit: int = Query(default=10, ge=0)) -> list[GetGoodsResponse]:
    goods = await goods_query.execute(GetGoodsRequestDTO(offset=offset, limit=limit))
    return [GetGoodsResponse(id=good.id, name=good.name, category_name=good.category_name,
                             amount=good.amount, price=good.price) for good in goods]


@goods_router.post("/good", status_code=status.HTTP_201_CREATED, response_model=uuid.UUID)
async def add_goods(request: AddGoodRequest,
                    goods_command: AddGoodsCommand = Depends(get_goods_add_command)) -> uuid.UUID:
    return await goods_command.execute(
        AddGoodRequestDTO(name=request.name, category_name=request.category_name, price=request.price,
                          amount=request.amount))


@goods_router.post("/category", status_code=status.HTTP_201_CREATED, response_model=uuid.UUID)
async def add_category(request: AddGoodsCategoryRequest,
                       goods_category_command: AddGoodsCategoryCommand = Depends(
                           get_goods_category_add_command)) -> uuid.UUID:
    return await goods_category_command.execute(request.category_name)


@goods_router.put("/good/photo", status_code=status.HTTP_200_OK)
async def add_photos_to_good(good_id: uuid.UUID, files: list[UploadFile] = File(...)) -> None:
    photos = []
    for file in files:
        photos.append(Photo(content=await file.read(), filename=file.filename, content_type=file.content_type))
