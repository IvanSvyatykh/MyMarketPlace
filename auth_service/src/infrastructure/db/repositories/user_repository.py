from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError
from auth_service.src.domain.entity.user import User
from auth_service.src.domain.repositories.user_repository import UserRepositoryInterface
from auth_service.src.infrastructure.db.models import UserModel


class UserRepository(UserRepositoryInterface):

    def __init__(self, session: AsyncSession):
        self.__session = session

    async def add_user(self, user: User) -> None:
        try:
            await self.__session.execute(
                insert(UserModel).values(id=user.id, email=user.email, name=user.name, password=user.password))
            await self.__session.commit()
        except IntegrityError as e:
            await self.__session.rollback()
            raise e

    async def get_user_by_email(self, email: str) -> User | None:
        res = await  self.__session.execute(select(UserModel).where(UserModel.email == email))
        res = res.scalar_one_or_none()
        return User(id=res.id, name=res.name, email=res.email, password=res.password) if res else None
