from abc import ABC, abstractmethod
from typing import Optional, Sequence
from src.modules.projects.application.dtos import ProjectCreateDTO
from src.modules.projects.domain.entities import Project


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
