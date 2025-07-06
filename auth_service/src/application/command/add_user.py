from sqlalchemy.exc import IntegrityError

from auth_service.src.application.dto.user import AddUserRequestDTO
from auth_service.src.domain.repositories.user_repository import UserRepositoryInterface
from auth_service.src.domain.entity.user import User

class AddUserCommand:

    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository



    async def execute(self, user: AddUserRequestDTO)->None:
        user = User(email=user.email , name=user.name , password=user.password)
        try:
            await self.__user_repository.add_user(user)
        except IntegrityError as e:
            raise e

