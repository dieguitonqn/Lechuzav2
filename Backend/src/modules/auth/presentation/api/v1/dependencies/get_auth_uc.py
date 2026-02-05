from sqlmodel import Session
from src.modules.auth.application.use_cases.auth_uc import AuthUseCase
from src.modules.auth.infrastructure.repositories.auth_repo import AuthRepository
from src.database.database import get_session


async def get_auth_uc(db: Session = get_session()) -> AuthUseCase:
    auth_repository = AuthRepository(db)
    return AuthUseCase(auth_repository)