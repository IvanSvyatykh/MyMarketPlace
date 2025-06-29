import uuid


class Photo:
    def __init__(self, content: bytes, filename: str, content_type: str) -> None:
        self.__content = content
        self.__filename = str(uuid.uuid4()) + "." + filename.split('.')[-1]
        self.__content_type = content_type

    @property
    def content(self) -> bytes:
        return self.__content

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def content_type(self) -> str:
        return self.__content_type
