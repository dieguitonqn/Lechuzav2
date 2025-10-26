from abc import ABC, abstractmethod


class ITtalNpRepository(ABC):
    @abstractmethod
    async def create_ttal_np(
        self, project_id: str, codigo: str, asunto: str, ttal_np_file: str
    ):
        pass
