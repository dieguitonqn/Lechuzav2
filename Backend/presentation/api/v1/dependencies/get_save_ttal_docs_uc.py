from infrastructure.database.database import get_session
from fastapi import Depends
from sqlmodel import Session


def get_save_ttal_and_docs_uc(session: Session = Depends(get_session)):
    from application.use_cases.ttal_and_docs_uc import SaveTtalAndDocsUseCase
    from infrastructure.repositories.ttal_np_repo import SQLModelTtalNpRepository
    from infrastructure.repositories.document_repo import SQLModelDocumentRepository
    from infrastructure.storage.file_managment_repo import FileManager

    ttal_np_repo = SQLModelTtalNpRepository(session)
    document_repo = SQLModelDocumentRepository(session)
    file_manager = FileManager()
    return SaveTtalAndDocsUseCase(ttal_np_repo, document_repo, file_manager)
