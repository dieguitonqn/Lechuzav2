

from fastapi import Depends
from sqlmodel import Session
from src.modules.documents.infrastructure.ttals_nps_repo import Ttal_nps_Repository
from src.modules.documents.application.uc_documents import DocumentsUC
from src.infrastucture.database.database import get_session
from src.modules.documents.infrastructure.documents_repo import DocumentsRepository
from src.modules.documents.infrastructure.documents_files_repo import DocumentsFilesRepo



def get_document_uc(session: Session = Depends(get_session)) -> DocumentsUC:
    # Aquí puedes inicializar tu repositorio y luego el caso de uso
    documents_repo = DocumentsRepository(session)
    files_repo = DocumentsFilesRepo()
    ttal_nps_repo = Ttal_nps_Repository(session)
    # document_repository = DocumentRepository()

    return DocumentsUC(documents_repo, files_repo, ttal_nps_repo)
    