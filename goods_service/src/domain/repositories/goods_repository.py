from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from ..enteties.good import Good
from ..agregates.good import Good as GoodAggregate


class GoodsRepositoryInterface(ABC):

    @abstractmethod
    def __init__(self, session: AsyncSession):
        raise NotImplementedError()

    @abstractmethod
    async def get_goods(self, offset: int, limit: int) -> list[GoodAggregate]:
        raise NotImplementedError()

    @abstractmethod
    async def add_good(self, good: Good) -> None:
        raise NotImplementedError()
