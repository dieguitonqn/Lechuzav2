from abc import ABC, abstractmethod
from application.dtos.projects_dto import ProjectCreateDTO
from domain.entities.projects import Project


class IProject(ABC):
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
