from abc import ABC, abstractmethod

from goods_service.src.domain.agregates.good_photo import GoodPhoto


class GoodsPhotosRepositoryInterface(ABC):

    @abstractmethod
    async def add_photo(self, photo: GoodPhoto) -> None:
        raise NotImplementedError()
