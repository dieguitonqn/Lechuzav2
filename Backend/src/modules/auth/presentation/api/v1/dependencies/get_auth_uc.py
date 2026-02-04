from sqlmodel import Session
from ..application.use_cases.auth_uc import AuthUseCase
from ..infrastructure.repositories.auth_repo import AuthRepository
from infrastructure.database.database import get_session


async def get_auth_uc(db: Session = get_session()) -> AuthUseCase:
    auth_repository = AuthRepository(db)
    return AuthUseCase(auth_repository)