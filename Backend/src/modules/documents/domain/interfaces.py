from abc import ABC
from src.domain.entities.documents import Document


class IDocumentsRepository(ABC):
    def save_document_toDB(self, document, user):
        pass

    def read_documents_fromDB(self, project_id, from_idx, to_idx) -> list[Document]:
        pass

    def get_documents_paginated(
        self,
        project_id: str,
        offset: int = 1,
        limit: int = 10,
        name_filter: str = None,
        code_filter: str = None,
        revision_filter: str = None,
        np_ttal_filter: str = None,
        status_filter: str = None,
        fecha_ingreso_filter: str = None,
        correction_report_filter: str = None
    ) -> list[Document]:
        pass

    def count_documents_by_project(self, project_id: str) -> int:
        pass


class IDocsFilesRepository(ABC):
    async def save_file(self, file, filename):
        pass

    async def get_file(self, filename):
        pass

    async def delete_file(self, filename):
        pass

    async def update_file(self, filename, new_file):
        pass


class ITransmittalNPRepository(ABC):
    async def save_transmittal_np_file(self, ttal_dto, user) -> str:
        pass

    async def save_transmittal_np_toDB(self, ttal_np, user):
        pass
