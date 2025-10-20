from infrastructure.database.database import get_session
from fastapi import Depends
from sqlmodel import Session


def get_project_uc(session: Session = Depends(get_session)):
    from application.use_cases.projects_uc import ProjectUseCase
    from infrastructure.repositories.project_repo import SQLModelProjectRepository
    from infrastructure.storage.file_managment_repo import FileManager

    project_repository = SQLModelProjectRepository(session)
    file_manager = FileManager()
    return ProjectUseCase(project_repository, file_manager)