from abc import ABC, abstractmethod


from Backend.src.domain.entities.users import User


class IAuthorization(ABC):
    @abstractmethod
    async def get_current_user(self, user_id: int) -> User:
        pass