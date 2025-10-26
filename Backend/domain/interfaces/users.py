from abc import ABC, abstractmethod
from typing import Sequence, Optional
from domain.entities.users import User


class IUserRepository(ABC):
    @abstractmethod
    def create_user(
        self,
        email: str,
        password: str,
        is_active: bool = False,
        is_epen_user: bool = False,
        is_admin: bool = False,
    ) -> User:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    def list_users(self) -> Sequence[User]:
        pass
