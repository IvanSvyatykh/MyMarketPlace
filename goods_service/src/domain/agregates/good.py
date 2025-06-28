import uuid
from ..enteties.good_category import GoodCategory


class Good:

    def __init__(self, good_category: GoodCategory, name: str, amount: int, price: float,
                 id: uuid.UUID | None = None) -> None:
        self.__good_category = good_category
        self.__name = name
        self.__price = price
        self.__amount = amount
        self.__id = id

    async def generate_id(self) -> None:
        self.__id = uuid.uuid4()

    @property
    def id(self) -> uuid.UUID | None:
        return self.__id

    @property
    def category_id(self) -> uuid.UUID | None:
        return self.__good_category.id

    @property
    def category_name(self) -> str | None:
        return self.__good_category.name

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def amount(self) -> int:
        return self.__amount
