from sqlalchemy.exc import IntegrityError

from goods_service.src.domain.repositories.s3_repository import S3RepositoryInterface
from goods_service.src.application.dto.goods import AddGoodPhotoRequestDTO
from goods_service.src.domain.repositories.goods_photos_repository import GoodsPhotosRepositoryInterface
from goods_service.src.domain.agregates.good_photo import GoodPhoto
from goods_service.src.domain.enteties.photo import Photo


class AddPhotosToGoodUsecase:

    def __init__(self, s3_repository: S3RepositoryInterface, good_photos_repository: GoodsPhotosRepositoryInterface):
        self.__s3_repository = s3_repository
        self.__good_photos_repository = good_photos_repository

    async def execute(self, add_photo: AddGoodPhotoRequestDTO) -> None:
        photo = Photo(content=add_photo.photo.content, filename=add_photo.photo.filename,
                      content_type=add_photo.photo.content_type)
        photo_url = await self.__s3_repository.upload_file(bucket_name=str(add_photo.good_id),
                                                           file_bytes=photo.content,
                                                           object_name=photo.filename)
        good_photo = GoodPhoto(photo_url=photo_url, description=add_photo.description, good_id=add_photo.good_id,
                               photo=photo)
        try:
            await self.__good_photos_repository.add_photo(good_photo)
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e
