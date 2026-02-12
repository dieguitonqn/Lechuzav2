from fastapi import Depends
from sqlmodel import Session
from src.infrastucture.database.database import get_session
from src.modules.projects.application.use_cases import ProjectUseCase
from src.modules.projects.infrastructure.project_repo import SQLModelProjectRepository
from src.modules.projects.infrastructure.file_manager_repo import FileManager


def get_project_uc(session: Session = Depends(get_session)):
    """Dependency that returns a ProjectUseCase bound to a DB session."""
    project_repository = SQLModelProjectRepository(session)
    file_manager = FileManager()
    return ProjectUseCase(project_repository, file_manager)