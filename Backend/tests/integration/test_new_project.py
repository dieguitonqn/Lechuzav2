import pytest
from sqlmodel import SQLModel, Session, create_engine
from infrastructure.database.database import get_session
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="session")
def test_engine():
    """Engine de test usando PostgreSQL con base de datos de test"""
    # URL para la base de datos de test en Docker Compose
    test_db_url = "postgresql://test_user:test_pass@localhost:5433/test_db"

    engine = create_engine(test_db_url, echo=False)

    # Crear tablas para tests
    SQLModel.metadata.create_all(engine)

    yield engine

    # Limpiar tablas después de todos los tests
    SQLModel.metadata.drop_all(engine)


@pytest.fixture
def test_client(test_engine):
    """TestClient con base de datos de test"""

    # Override la dependencia de sesión para usar el engine de test
    def get_test_session():
        with Session(test_engine) as session:
            yield session

    app.dependency_overrides[get_session] = get_test_session

    with TestClient(app) as client:
        yield client

    # Limpiar override
    app.dependency_overrides.clear()


def test_create_project_success(test_client):
    # Primero, crear una compañía para asociar al proyecto
    company_response = test_client.post(
        "/api/v1/companies/", json={"name": "Associated Company", "code": "AC123"}
    )
    assert company_response.status_code == 201
    company_data = company_response.json()
    company_id = company_data["id"]
    project_file = {
        "project_file": ("test.pdf", b"Dummy PDF content", "application/pdf")
    }

    response = test_client.post(
        "/api/v1/projects/",
        data={
            "name": "Test Project",
            "code": "TP123",
            "description": "A project for testing",
            "company_id": company_id,
        },
        files=project_file,
    )
    assert response.status_code == 201
    data = response.json()
    assert data["message"] == "Project created successfully"
