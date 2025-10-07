from infrastructure.repositories.document_repo import SQLModelDocumentRepository

from unittest.mock import patch
import pytest
from models.documents import Document
from database.database import get_session
from sqlmodel import Session

@pytest.fixture
def document_repo():
    session:Session=get_session()
    return SQLModelDocumentRepository(session)

def test_create_document_success(document_repo):
   
    document = Document(
        codigo="DOC-001",
        nombre="Documento 1",
        revision="A",
        document_file="doc_file_1",
        project_id="1234",
        ttal_np_id=None
    )
    result = document_repo.create_document(document)

    assert result is not None
    assert result.id is not None
    assert result.codigo == "DOC-001"
    assert result.nombre == "Documento 1"
