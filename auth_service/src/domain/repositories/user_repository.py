from abc import ABC, abstractmethod
from auth_service.src.domain.entity.user import User


class UserRepositoryInterface(ABC):

    @abstractmethod
    async def add_user(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_email(self, email: str) -> User | None:
        raise NotImplementedError
