from pathlib import Path
from application.dtos.projects_dto import ProjectCreateDTO
from domain.interfaces.projects_inteface import IProject
from infrastructure.storage.file_managment_repo import IFileManager
from domain.entities.projects import Project
from typing import Optional, Sequence


class ProjectUseCase:
    def __init__(self, project_repo: IProject, file_manager: IFileManager):
        self.project_repo = project_repo
        self.file_manager = file_manager

    async def create_project(self, project_dto: ProjectCreateDTO) -> Optional[Project]:
        # Primero guardar el proyecto en base de datos
        project: Optional[Project] = self.project_repo.create_project(project_dto)
        if not project:
            raise Exception("Failed to create project")

        # Luego guardar el archivo en el sistema de archivos con el UUID del proyecto

        project_file_dir = Path("files") / str(project.id)
        project_file_path = await self.file_manager.save_file(
            file=project_dto.project_file, destination_path=str(project_file_dir)
        )
        if not project_file_path:
            raise Exception("Failed to save project file")

        # Finalmente actualizar el registro del proyecto con la ruta del archivo guardado

        updated_project: Optional[Project] = self.project_repo.add_project_file(
            project_id=str(project.id), file_path=project_file_path
        )
        if not updated_project:
            raise Exception("Failed to update project with file path")
        return updated_project

    def get_project(self, project_id: str) -> Optional[Project]:
        project: Optional[Project] = self.project_repo.get_project(project_id)
        if not project:
            raise Exception("Project not found")
        return project

    def list_projects(self) -> Optional[Sequence[Project]]:
        projects: Optional[Sequence[Project]] = self.project_repo.list_projects()
        return projects
