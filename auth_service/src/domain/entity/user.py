import uuid


class User:

    def __init__(self, email: str, name: str, password: str, id: uuid.UUID = None) -> None:
        self.__email = email
        self.__name = name
        self.__password = password
        self.__id = id if id else uuid.uuid4()

    @property
    def id(self) -> uuid.UUID:
        return self.__id

    @property
    def email(self) -> str:
        return self.__email

    @property
    def name(self) -> str:
        return self.__name

    @property
    def password(self) -> str:
        return self.__password
