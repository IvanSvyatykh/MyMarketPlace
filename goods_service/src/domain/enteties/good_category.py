import uuid


class GoodCategory:
    id: uuid.UUID | None
    name: str

    def __init__(self, name: str | None, id: uuid.UUID | None = None):
        self.__id = id
        self.__name = name

    async def generate_id(self) -> None:
        self.__id = uuid.uuid4()

    @property
    def id(self) -> uuid.UUID | None:
        return self.__id

    @property
    def name(self) -> str | None:
        return self.__name
