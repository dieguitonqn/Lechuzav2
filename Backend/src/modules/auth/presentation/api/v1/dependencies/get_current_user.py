from typing import Optional
from fastapi import Depends, HTTPException, status, Header
from sqlmodel import Session
from src.infrastucture.database.database import get_session
from src.modules.auth.infrastructure.auth_repo import AuthRepository
from src.domain.entities.users import User


async def get_current_user(
    db: Session = Depends(get_session),
    authorization: Optional[str] = Header(None)
) -> User:
    """
    Dependency to get current authenticated user from JWT token.
    Verifies the Authorization header and returns the user.
    Raises HTTPException if authentication fails.
    """
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing"
        )
    
    # Extract token from "Bearer <token>" format
    token = authorization.split(" ")[1] if " " in authorization else None
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header format"
        )
    
    # Create auth repository and verify token directly
    auth_repository = AuthRepository(db)
    
    # Verify token and get user
    user = await auth_repository.verify_access_token(token)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    return user
