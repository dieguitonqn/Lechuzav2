from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID
from ..entities.auth_token import AuthToken
from src.domain.entities.users import User


class IAuthRepository(ABC):
    @abstractmethod
    async def authenticate_user(self, email: str, password: str) -> Optional[AuthToken]:
        pass
    
    @abstractmethod
    async def refresh_token(self, refresh_token: str) -> Optional[AuthToken]:
        pass
    
    @abstractmethod
    async def verify_access_token(self, token: str) -> Optional[User]:
        """Verify access token and return user if valid"""
        pass