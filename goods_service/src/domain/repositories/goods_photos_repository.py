from abc import ABC, abstractmethod

from goods_service.src.domain.enteties.photo import Photo


class GoodsPhotosRepositoryInterface(ABC):

    @abstractmethod
    async def add_photo(self, photo: Photo) -> Photo:
        raise NotImplementedError()