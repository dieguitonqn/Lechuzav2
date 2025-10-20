from infrastructure.repositories.document_repo import SQLModelDocumentRepository

from unittest.mock import patch
import pytest
from domain.entities.documents import Document
from infrastructure.database.database import get_session
from sqlmodel import Session

# @pytest.fixture
# def document_repo():
#     session:Session=next(get_session())
#     return SQLModelDocumentRepository(session)
@pytest.mark.skip("This test file is deprecated and will be removed in future versions.")
def test_create_document_success(document_repo):


    result = document_repo.create_document(
        codigo = 'DOC-001',
        nombre = 'Documento 1',
        revision = 'A',
        document_file = 'path/to/document.pdf   ',
        project_id = '123e4567-e89b-12d3-a456-426614174000',
        ttal_np_id= '123e4567-e89b-12d3-a456-426614174001'
    )

    assert result is not None
    assert result.id is not None
    assert result.codigo == "DOC-001"
    assert result.nombre == "Documento 1"
