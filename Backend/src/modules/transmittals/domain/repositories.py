from abc import ABC, abstractmethod


class ITtalNpRepository(ABC):
    @abstractmethod
    def create_ttal_np(
        self, project_id: str, codigo: str, asunto: str, ttal_np_file: str
    ):
        pass


class IDocumentRepository(ABC):
    @abstractmethod
    def create_document(
        self,
        codigo: str,
        nombre: str,
        revision: str,
        document_file: str,
        project_id: str = "",
        ttal_np_id: str = "",
    ):
        pass
