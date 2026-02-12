from sqlmodel import Session, select
from typing import Optional, Sequence
from fastapi import Depends
from src.infrastucture.database.database import get_session
from src.modules.projects.application.dtos import ProjectCreateDTO
from src.modules.projects.domain.interfaces import IProject
from src.domain.entities.projects import Project
from src.domain.entities.models_links import ProjectUserLink


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

    def list_projects(self, user_id: str) -> Optional[Sequence[Project]]:
        user_projects_links: Optional[Sequence[ProjectUserLink]] = self.session.exec(
            select(ProjectUserLink).where(ProjectUserLink.user_id == user_id)
        ).all()
        project_ids = [link.project_id for link in user_projects_links]
        
        projects: Optional[Sequence[Project]] = self.session.exec(select(Project).where(Project.id.in_(project_ids))).all()
        return projects
