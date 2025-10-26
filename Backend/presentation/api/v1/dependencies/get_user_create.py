from fastapi import Depends
from infrastructure.database.database import get_session
from sqlmodel import Session
from application.use_cases.users_uc import CreateUserUseCase
from infrastructure.repositories.users_repo import (
    SQLModelUserRepository as UserRepository,
)


def get_user_create_use_case(session: Session = Depends(get_session)):
    """Dependency that returns a CreateUserUseCase bound to a DB session.

    Using Depends for the session ensures FastAPI treats the session as a sub-dependency
    and does not attempt to validate/serialize the Session type as a Pydantic field.
    """
    user_repository = UserRepository(session)
    return CreateUserUseCase(user_repository)
