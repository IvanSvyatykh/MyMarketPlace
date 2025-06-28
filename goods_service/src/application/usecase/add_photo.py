from goods_service.src.domain.repositories.s3_repository import S3RepositoryInterface


class AddPhotosToGood:

    def __init__(self, s3_repository: S3RepositoryInterface, ):
        self.__s3_repository = s3_repository
