import pytest
from fastapi import status
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, AsyncMock
from presentation.api.v1.endpoints.ttal_np_documents import ttal_documents
from main import app
import uuid


@pytest.fixture
def client():
    """
    Cliente de prueba que usa la app principal para que los dependency overrides funcionen.
    """
    # from main import app

    app.include_router(ttal_documents)  # Asegurarse que el router esté incluido

    with TestClient(app) as client:
        yield client


@pytest.fixture
def mock_save_ttal_and_docs_uc():
    """
    Mockea la dependencia get_save_ttal_and_docs_uc usada en el endpoint de ttal-docs.
    Devuelve un MagicMock con execute configurado para simular éxito.
    """
    mock_uc = MagicMock()
    mock_uc.execute.return_value = None  # Simula que no retorna nada (éxito)
    return mock_uc


@pytest.fixture
def ov_get_save_ttal_and_docs_uc():
    """Override del Use Case de salvado de transmittal y documentos"""
    from src.modules.transmittals.presentation.dependencies import (
        get_save_ttal_and_docs_uc,
    )

    mock_uc = AsyncMock()
    # Configurar el mock para que execute devuelva una corrutina exitosa
    mock_uc.execute.return_value = None

    app.dependency_overrides[get_save_ttal_and_docs_uc] = lambda: mock_uc

    yield mock_uc

    # Limpiar override después del test
    app.dependency_overrides.pop(get_save_ttal_and_docs_uc, None)


def test_upload_ttal_document_success(client, ov_get_save_ttal_and_docs_uc):
    """
    Test para la subida exitosa de un transmittal y documentos.
    Nota: TestClient tiene limitaciones con List[UploadFile], así que este test
    verifica principalmente que el endpoint puede procesar la estructura básica.
    """
    # Test con un solo documento para simplificar
    test_project_id = str(uuid.uuid4())
    data = {
        "project_id": test_project_id,
        "ttal_np_code": "TTAL-001",
        "ttal_np_description": "Test transmittal",
        "document_code": ["DOC-001"],  # Un solo valor
        "document_name": ["Document 1"],
        "document_revision": ["A"],
    }

    files = {
        "ttal_np_file": ("ttal.pdf", b"file content", "application/pdf"),
        "document_file": ("doc1.pdf", b"document 1 content", "application/pdf"),
    }

    response = client.post("/api/v1/ttal-docs/", data=data, files=files)

    # Ahora debería funcionar correctamente con AsyncMock
    assert response.status_code == status.HTTP_201_CREATED
    response_data = response.json()
    assert response_data["message"] == "Transmittal and documents uploaded successfully"

    # Verificar que el use case fue llamado
    ov_get_save_ttal_and_docs_uc.execute.assert_called_once()


def test_upload_ttal_document_missing_fields(client, ov_get_save_ttal_and_docs_uc):
    """
    Test para verificar que el endpoint maneja correctamente campos faltantes.
    """
    # Datos incompletos - falta ttal_np_description
    test_project_id = str(uuid.uuid4())
    data = {
        "project_id": test_project_id,
        "ttal_np_code": "TTAL-001",
        # 'ttal_np_description': 'Test transmittal',  # Campo faltante
        "document_code": ["DOC-001"],
        "document_name": ["Document 1"],
        "document_revision": ["A"],
    }

    files = {
        "ttal_np_file": ("ttal.pdf", b"file content", "application/pdf"),
        "document_file": ("doc1.pdf", b"document 1 content", "application/pdf"),
    }

    response = client.post("/api/v1/ttal-docs/", data=data, files=files)

    # Debería devolver 422 por campo faltante requerido
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_upload_ttal_document_mismatched_lists(client, ov_get_save_ttal_and_docs_uc):
    """
    Test para verificar que el endpoint maneja listas desbalanceadas.
    """
    # Listas con diferentes tamaños - usando el formato esperado (CSV en strings)
    test_project_id = str(uuid.uuid4())
    data = {
        "project_id": test_project_id,
        "ttal_np_code": "TTAL-001",
        "ttal_np_description": "Test transmittal",
        "document_code": "DOC-001,DOC-002",  # 2 elementos (CSV)
        "document_name": "Document 1",  # 1 elemento
        "document_revision": "A",  # 1 elemento
    }

    files = {
        "ttal_np_file": ("ttal.pdf", b"file content", "application/pdf"),
        "document_file": ("doc1.pdf", b"document 1 content", "application/pdf"),
    }

    response = client.post("/api/v1/ttal-docs/", data=data, files=files)

    # Debería devolver 400 por listas desbalanceadas
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    response_data = response.json()
    assert "Mismatched document fields" in response_data["detail"]


def test_upload_ttal_document_use_case_error(client, ov_get_save_ttal_and_docs_uc):
    """
    Test para verificar que el endpoint maneja errores del use case.
    """
    # Configurar el mock para que lance una excepción
    ov_get_save_ttal_and_docs_uc.execute.side_effect = Exception(
        "Database connection error"
    )

    test_project_id = str(uuid.uuid4())
    data = {
        "project_id": test_project_id,
        "ttal_np_code": "TTAL-001",
        "ttal_np_description": "Test transmittal",
        "document_code": ["DOC-001"],
        "document_name": ["Document 1"],
        "document_revision": ["A"],
    }

    files = {
        "ttal_np_file": ("ttal.pdf", b"file content", "application/pdf"),
        "document_file": ("doc1.pdf", b"document 1 content", "application/pdf"),
    }

    response = client.post("/api/v1/ttal-docs/", data=data, files=files)

    # Debería devolver 500 cuando el use case falla
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    response_data = response.json()
    assert "Database connection error" in response_data["detail"]
