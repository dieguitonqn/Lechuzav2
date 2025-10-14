from abc import ABC, abstractmethod
from core.dtos.projects_dto import ProjectCreateDTO
from models.projects import Project
class IProject:
    @abstractmethod
    async def create_project(self, project: ProjectCreateDTO) -> Project:
        
        pass

    @abstractmethod
    async def add_project_file(self, project_id: str, file_path: str) -> Project:
        pass

    @abstractmethod
    async def get_project(self, project_id: str) -> Project:
        pass

    @abstractmethod
    async def list_projects(self) -> list[Project]:
        pass
