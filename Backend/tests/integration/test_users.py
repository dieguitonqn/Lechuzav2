import pytest
from fastapi.testclient import TestClient
from fastapi import status
from main import app
from sqlmodel import SQLModel, Session, create_engine
from infrastructure.database.database import get_session
from domain.entities.users import User


@pytest.fixture
def test_engine():
    """Engine de test usando PostgreSQL con base de datos de test"""
    # URL para la base de datos de test en Docker Compose
    test_db_url = "postgresql://test_user:test_pass@localhost:5433/test_db"

    engine = create_engine(test_db_url, echo=False)
    SQLModel.metadata.drop_all(engine)

    # Crear tablas para tests
    SQLModel.metadata.create_all(engine)

    yield engine

    # Limpiar tablas después de todos los tests
    SQLModel.metadata.drop_all(engine)


@pytest.fixture
def db_session(test_engine):
    """Sesión de base de datos para cada test"""
    with Session(test_engine) as session:
        yield session
        session.rollback()  # Asegura que los cambios no persistan entre tests


@pytest.fixture
def client(db_session):
    """Cliente de test de FastAPI con sesión de base de datos inyectada"""

    def get_test_session():
        yield db_session

    app.dependency_overrides[get_session] = get_test_session
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


def test_create_user_success(client):
    """Test de integración para crear un nuevo usuario exitosamente"""
    response = client.post(
        "api/v1/users/",
        data={
            "email": "test@example.com",
            "password": "testpassword",
        },
    )
    assert response.status_code == 201
    json_response = response.json()
    assert json_response["email"] == "test@example.com"
    assert json_response["is_active"] is False
    assert json_response["is_admin"] is False
    assert json_response["is_epen_user"] is False


def test_create_user_missing_fields(client):
    """Test de integración para crear un usuario con campos faltantes"""
    response = client.post(
        "api/v1/users/",
        data={
            "email": "",
            "password": "testpassword",
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_user_duplicate_email(client, db_session):
    """Test de integración para crear un usuario con email duplicado"""
    # Crear el primer usuario
    user_test = User(
        email="test@example.com",
        password_hash="testpassword",
    )
    db_session.add(user_test)
    db_session.commit()
    db_session.refresh(user_test)

    # Intentar crear un segundo usuario con el mismo email
    response2 = client.post(
        "api/v1/users/",
        data={
            "email": "test@example.com",
            "password": "testpassword",
        },
    )
    assert response2.status_code == status.HTTP_400_BAD_REQUEST
