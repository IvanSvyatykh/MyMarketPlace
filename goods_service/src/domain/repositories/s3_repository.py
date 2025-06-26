from abc import ABC, abstractmethod


class S3RepositoryInterface(ABC):

    @abstractmethod
    async def upload_file(self, bucket_name: str, file_bytes: bytes, object_name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_file(self, bucket_name: str, object_name: str) -> bytes:
        pass

    @abstractmethod
    async def get_files(self, bucket_name: str) -> list[bytes]:
        pass

    @abstractmethod
    async def delete_file(self, bucket_name: str, object_name: str) -> None:
        pass
