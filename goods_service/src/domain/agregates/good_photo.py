import uuid

from goods_service.src.domain.enteties.photo import Photo


class GoodPhoto:

    def __init__(self, photo: Photo, description: str, good_id: uuid.UUID, photo_url: str) -> None:
        self.__id = uuid.uuid4()
        self.__photo_url = photo_url
        self.__photo = photo
        self.__description = description
        self.__good_id = good_id

    @property
    def id(self) -> uuid.UUID:
        return self.__id

    @property
    def photo_url(self) -> str:
        return self.__photo_url

    @property
    def good_id(self) -> uuid.UUID:
        return self.__good_id

    @property
    def description(self) -> str:
        return self.__description

    @property
    def photo_content(self) -> bytes:
        return self.__photo.content

    @property
    def content_type(self) -> str:
        return self.__photo.content_type

    @property
    def filename(self) -> str:
        return self.__photo.filename
