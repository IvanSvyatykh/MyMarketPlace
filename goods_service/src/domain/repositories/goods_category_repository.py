from abc import abstractmethod, ABC
from ..enteties.goods_category import GoodCategory

from sqlalchemy.ext.asyncio import AsyncSession


class GoodsCategoryRepositoryInterface(ABC):

    @abstractmethod
    def __init__(self, session: AsyncSession):
        raise NotImplementedError

    @abstractmethod
    async def get_category_by_name(self, name: str) -> GoodCategory | None:
        raise NotImplementedError

    @abstractmethod
    async def add_category(self, category: GoodCategory) -> GoodCategory:
        raise NotImplementedError
