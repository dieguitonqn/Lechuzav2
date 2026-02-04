from fastapi import Depends
from sqlmodel import Session
from infrastructure.database.database import get_session
from src.modules.users.application.use_cases import CreateUserUseCase
from src.modules.users.infrastructure.repository_impl import SQLModelUserRepository


def get_user_create_use_case(session: Session = Depends(get_session)):
    """Dependency that returns a CreateUserUseCase bound to a DB session.

    Using Depends for the session ensures FastAPI treats the session as a sub-dependency
    and does not attempt to validate/serialize the Session type as a Pydantic field.
    """
    user_repository = SQLModelUserRepository(session)
    return CreateUserUseCase(user_repository)
