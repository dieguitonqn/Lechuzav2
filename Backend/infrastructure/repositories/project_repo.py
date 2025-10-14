from sqlmodel import Session, select
from core.dtos.projects_dto import ProjectCreateDTO
from core.interfaces.projects_inteface import IProject
from models.projects import Project

class SQLModelProjectRepository(IProject):
    def __init__(self, session: Session):
        self.session = session

    def create_project(self, project: ProjectCreateDTO) -> Project:
        new_project = Project(
            nombre=project.name,
            descripcion=project.description,
            codigo=project.code,
            company_id=project.company_id,
            project_file=""  # Inicialmente vacío, se actualizará después de guardar el archivo
        )
        self.session.add(new_project)
        self.session.commit()
        self.session.refresh(new_project)
        return new_project
    
    def add_project_file(self, project_id: str, file_path: str) -> Project:
        project: Project = self.session.get(Project, project_id)
        if not project:
            return None
        project.contrato_url = str(file_path)
        self.session.add(project)
        self.session.commit()
        self.session.refresh(project)
        return project
    
    def get_project(self, project_id: str) -> Project:
        project: Project = self.session.get(Project, project_id)
        return project
    
    def list_projects(self) -> list[Project]:
        projects: list[Project] = self.session.exec(select(Project)).all()
        return projects