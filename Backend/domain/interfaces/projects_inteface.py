from abc import ABC, abstractmethod
from application.dtos.projects_dto import ProjectCreateDTO
from domain.entities.projects import Project
from typing import Optional, Sequence


class IProject(ABC):
    @abstractmethod
    def create_project(self, project: ProjectCreateDTO) -> Optional[Project]:
        pass

    @abstractmethod
    def add_project_file(self, project_id: str, file_path: str) -> Optional[Project]:
        pass

    @abstractmethod
    def get_project(self, project_id: str) -> Optional[Project]:
        pass

    @abstractmethod
    def list_projects(self) -> Optional[Sequence[Project]]:
        pass
