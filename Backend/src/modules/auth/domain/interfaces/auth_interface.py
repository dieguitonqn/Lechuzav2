from abc import ABC, abstractmethod
from typing import Optional
from ..entities.auth_token import AuthToken


class IAuthRepository(ABC):
    @abstractmethod
    async def authenticate_user(self, email: str, password: str) -> Optional[AuthToken]:
        pass
    
    @abstractmethod
    async def refresh_token(self, refresh_token: str) -> Optional[AuthToken]:
        pass