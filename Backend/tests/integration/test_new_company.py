import pytest
from fastapi.testclient import TestClient
from main import app
from sqlmodel import SQLModel, Session, create_engine
from infrastructure.database.database import get_session


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


def test_create_company_success(test_client):
    response = test_client.post(
        "/api/v1/companies/", json={"name": "Test Company", "code": "TC123"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["message"] == "Company created successfully"
    assert data["name"] == "Test Company"
    assert data["codigo"] == "TC123"
    assert "id" in data
