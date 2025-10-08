from database.database import get_session
from sqlmodel import Session
from core.use_cases.create_user import CreateUserUseCase
from infrastructure.repositories.users_repo import SQLModelUserRepository as UserRepository

def get_user_create_use_case(session:Session) -> CreateUserUseCase:
    user_repository = UserRepository(session)
    return CreateUserUseCase(user_repository)
