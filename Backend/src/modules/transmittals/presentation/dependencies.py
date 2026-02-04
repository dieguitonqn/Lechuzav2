from src.modules.transmittals.application.use_cases import SaveTtalAndDocsUseCase
from src.modules.transmittals.infrastructure.repository_impl import (
    SQLModelTtalNpRepository,
    SQLModelDocumentRepository,
)
from infrastructure.storage.file_managment_repo import FileManager


def get_save_ttal_and_docs_uc() -> SaveTtalAndDocsUseCase:
    ttal_repo = SQLModelTtalNpRepository()
    document_repo = SQLModelDocumentRepository()
    file_manager = FileManager()
    return SaveTtalAndDocsUseCase(
        ttal_repo=ttal_repo,
        document_repo=document_repo,
        file_manager=file_manager,
    )
