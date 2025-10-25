import uuid
import pytest
from main import app
from fastapi.testclient import TestClient
from fastapi import status, UploadFile
from unittest.mock import MagicMock
from presentation.api.v1.endpoints.projects import projects



@pytest.fixture
def client():
    from main import app
    app.include_router(projects)
    with TestClient(app) as client:
        yield client


@pytest.fixture
def mock_get_project_uc():
    project_mock = MagicMock()
    project_mock.id = uuid.uuid4()
    project_uc_mock = MagicMock()
    project_uc_mock.create_project.return_value = project_mock
    return project_uc_mock


@pytest.fixture
def ov_get_project_uc(mock_get_project_uc):
    from presentation.api.v1.dependencies.get_proyect_uc import get_project_uc

    app.dependency_overrides[get_project_uc] = lambda: mock_get_project_uc
    try:
        yield mock_get_project_uc
    finally:
        app.dependency_overrides.pop(get_project_uc, None)


def test_create_project(client, ov_get_project_uc):
    # Datos del formulario
    form_data = {
        "name": "Loma",
        "code": "1234",
        "description": "Aguante Loma",
        "company_id": str(uuid.uuid4())  # UUID como string
    }

    # Archivo para upload - formato correcto para TestClient
    files = {
        "project_file": ("primero.pdf", b"Contenido del archivo", "application/pdf")
    }

    # response es un objeto Response HTTP, no un Project
    response = client.post('/projects/', data=form_data, files=files)

    # Verificar el status code
    assert response.status_code == status.HTTP_201_CREATED

    # Parsear la respuesta JSON
    response_data = response.json()

    # Verificar la estructura de la respuesta
    assert response_data["message"] == "Project created successfully"
    assert "project" in response_data

    # Verificar que el project ID es un UUID válido
    project_id = response_data["project"]
    assert isinstance(project_id, str)  # El JSON serializa UUID como string

    try:
        project_uuid = uuid.UUID(project_id)
        assert isinstance(project_uuid, uuid.UUID)
    except ValueError:
        pytest.fail("No es un uuid")

    # Verificar que el mock fue llamado correctamente
    ov_get_project_uc.create_project.assert_called_once()

def test_create_project_excep(client, ov_get_project_uc):
    ov_get_project_uc.create_project.side_effect = Exception("Error creating project")
    form_data = {
        "name": "Loma",
        "code": "1234",
        "description": "Aguante Loma",
        "company_id": str(uuid.uuid4())  # UUID como string
    }

    input_files = {
        "project_file": ("primero.pdf", b"Contenido del archivo", "application/pdf")
    }
    

    response = client.post('/projects/', data=form_data, files=input_files)
    assert response.status_code == 400


    response_data = response.json()
    assert response_data["detail"] == "Error creating project"
