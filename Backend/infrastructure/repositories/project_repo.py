from sqlmodel import Session, select
from application.dtos.projects_dto import ProjectCreateDTO
from domain.interfaces.projects_inteface import IProject
from domain.entities.projects import Project
from fastapi import Depends
from infrastructure.database.database import get_session
from typing import Optional, Sequence


class SQLModelProjectRepository(IProject):
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_project(self, project: ProjectCreateDTO) -> Optional[Project]:
        new_project = Project(
            nombre=project.name,
            descripcion=project.description,
            codigo=project.code,
            company_id=project.company_id,
            project_file="",  # Inicialmente vacío, se actualizará después de guardar el archivo
        )
        self.session.add(new_project)
        self.session.commit()
        self.session.refresh(new_project)
        return new_project

    def add_project_file(self, project_id: str, file_path: str) -> Optional[Project]:
        project: Optional[Project] = self.session.get(Project, project_id)
        if not project:
            return None
        project.contrato_url = str(file_path)
        self.session.add(project)
        self.session.commit()
        self.session.refresh(project)
        return project

    def get_project(self, project_id: str) -> Optional[Project]:
        project: Optional[Project] = self.session.get(Project, project_id)
        return project

    def list_projects(self) -> Optional[Sequence[Project]]:
        projects: Optional[Sequence[Project]] = self.session.exec(select(Project)).all()
        return projects
