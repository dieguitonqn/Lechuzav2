from typing import Optional
from src.modules.auth.domain.interfaces.auth_interface import IAuthRepository
from ..dtos.auth_dto import LoginResponse, UserResponse


class AuthUseCase:
    def __init__(self, auth_repository: IAuthRepository):
        self.auth_repository = auth_repository

    async def login(self, email: str, password: str) -> Optional[LoginResponse]:
        """
        Authenticate user and return access token
        """
        # Validate input
        if not email or not password:
            raise ValueError("Email and password are required")

        # Authenticate user
        auth_token = await self.auth_repository.authenticate_user(email, password)
        
        if not auth_token:
            return None

        # Convert to response DTO
        return LoginResponse(
            access_token=auth_token.access_token,
            refresh_token=auth_token.refresh_token,
            token_type=auth_token.token_type,
            user=UserResponse(
                id=auth_token.user.id,
                name=auth_token.user.name,
                email=auth_token.user.email,
                role=auth_token.user.role
            )
        )

    async def refresh_token(self, refresh_token: str) -> Optional[LoginResponse]:
        """
        Refresh access token using refresh token
        """
        if not refresh_token:
            raise ValueError("Refresh token is required")

        # Refresh token
        auth_token = await self.auth_repository.refresh_token(refresh_token)
        
        if not auth_token:
            return None

        # Convert to response DTO
        return LoginResponse(
            access_token=auth_token.access_token,
            refresh_token=auth_token.refresh_token,
            token_type=auth_token.token_type,
            user=UserResponse(
                id=auth_token.user.id,
                name=auth_token.user.name,
                email=auth_token.user.email,
                role=auth_token.user.role
            )
        )