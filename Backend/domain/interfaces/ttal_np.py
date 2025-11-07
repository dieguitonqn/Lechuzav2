from abc import ABC, abstractmethod
import uuid


class ITtalNpRepository(ABC):
    @abstractmethod
    def create_ttal_np(
        self, project_id: uuid.UUID, codigo: str, asunto: str, ttal_np_file: str
    ):
        pass
