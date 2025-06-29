from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from goods_service.src.domain.agregates.good_photo import GoodPhoto
from goods_service.src.domain.repositories.goods_photos_repository import GoodsPhotosRepositoryInterface
from goods_service.src.infrastructure.db.models.model import GoodsPhotosModel
from sqlalchemy import insert


class GoodPhotosRepository(GoodsPhotosRepositoryInterface):

    def __init__(self, session: AsyncSession):
        self.__session = session

    async def add_photo(self, photo: GoodPhoto) -> None:
        try:

            await self.__session.execute(
                insert(GoodsPhotosModel).values(id=photo.id, good_id=photo.good_id, description=photo.description,
                                                photo_url=photo.photo_url))
            await self.__session.commit()
        except IntegrityError as e:
            await self.__session.rollback()
            raise e
