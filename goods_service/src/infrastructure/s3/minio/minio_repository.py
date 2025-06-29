from io import BytesIO

from goods_service.src.domain.repositories.s3_repository import S3RepositoryInterface
from miniopy_async import Minio


class S3MinioRepository(S3RepositoryInterface):

    def __init__(self, minio_client: Minio):
        self.__minio_client = minio_client

    async def upload_file(self, bucket_name: str, file_bytes: bytes, object_name: str) -> str:
        if not await self.__minio_client.bucket_exists(bucket_name):
            await self.__minio_client.make_bucket(bucket_name=bucket_name)
        await self.__minio_client.put_object(
            bucket_name=bucket_name,
            object_name=object_name,
            data=BytesIO(file_bytes),
            length=len(file_bytes),
        )
        url = await self.__minio_client.presigned_get_object(bucket_name=bucket_name, object_name=object_name)
        return url

    async def get_file(self, bucket_name: str, object_name: str) -> bytes:
        async with await self.__minio_client.get_object(
                bucket_name=bucket_name,
                object_name=object_name,
        ) as response:
            bytes_content = await response.read()
            return bytes_content

    async def get_files(self, bucket_name: str) -> list[bytes]:
        bucket_objects = await self.__minio_client.list_objects(bucket_name=bucket_name)
        result = []
        for obj in bucket_objects:
            result.append(await self.get_file(bucket_name=bucket_name, object_name=obj.object_name))
        return result

    async def delete_file(self, bucket_name: str, object_name: str) -> None:
        await self.__minio_client.remove_object(bucket_name=bucket_name, object_name=object_name)
