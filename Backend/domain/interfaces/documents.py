from abc import ABC, abstractmethod


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
