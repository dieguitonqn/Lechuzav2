from sqlmodel import Session
from src.modules.auth.application.use_cases.auth_uc import AuthUseCase
from src.modules.auth.infrastructure.auth_repo import AuthRepository
from src.infrastucture.database.database import get_session
from fastapi import Depends


async def get_auth_uc(db: Session = Depends(get_session)) -> AuthUseCase:
    auth_repository = AuthRepository(db)
    return AuthUseCase(auth_repository)