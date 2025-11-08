from domain.entities.projects import Project
from domain.entities.statuses import Status
import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from infrastructure.database.database import get_session
from main import app


@pytest.fixture(scope="session")
def test_engine():
    """Engine de test usando PostgreSQL con base de datos de test"""
    # URL para la base de datos de test en Docker Compose
    test_db_url = "postgresql://test_user:test_pass@localhost:5433/test_db"

    engine = create_engine(test_db_url, echo=False)

    # Crear tablas para tests (sin drop previo para evitar conflictos)
    SQLModel.metadata.create_all(engine)

    yield engine

    # Limpiar tablas después de todos los tests
    SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_session(test_engine):
    """Sesión de base de datos para cada test"""
    with Session(test_engine) as session:
        # Asegurar que existe el Status con id=1 antes de cada test
        default_status = session.get(Status, 1)
        if not default_status:
            default_status = Status(
                id=1,
                nombre="EN REVISION",
                descripcion="Documento en proceso de revisión",
            )
            session.add(default_status)
            session.commit()

        yield session
        session.rollback()  # Asegura que los cambios no persistan entre tests


@pytest.fixture(scope="function")
def client(db_session):
    """Cliente de test de FastAPI con sesión de base de datos inyectada"""

    def get_test_session():
        yield db_session

    app.dependency_overrides[get_session] = get_test_session
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


def test_create_ttal_np_doc(client, db_session):
    """Test de integración para crear un nuevo Ttal NP Doc"""

    # Creo un proyecto de prueba
    project_data = {
        "name": "Test Project01",
        "description": "A project for testing",
    }
    project = Project(
        nombre=project_data["name"],
        codigo="TP001",
        descripcion=project_data["description"],
    )
    db_session.add(project)
    db_session.commit()
    db_session.refresh(project)

    # Enviar TODO como multipart con 'files'. Para campos no-archivo usar (None, valor)
    response = client.post(
        "/api/v1/ttal-docs/",
        files=[
            ("project_id", (None, str(project.id))),
            ("ttal_np_code", (None, "TTALNP001")),
            ("ttal_np_description", (None, "Test Transmittal NP Document")),
            # El endpoint actual toma el primer elemento y lo separa por comas
            ("document_code", (None, "DOC001,DOC002")),
            ("document_name", (None, "Document 1,Document 2")),
            ("document_revision", (None, "A,C")),
            # Archivos
            (
                "ttal_np_file",
                ("ttal_test.pdf", b"Test ttal file content", "application/pdf"),
            ),
            ("document_file", ("doc1.pdf", b"Test doc 1 content", "application/pdf")),
            ("document_file", ("doc2.pdf", b"Test doc 2 content", "application/pdf")),
        ],
    )
    if response.status_code != 201:
        # Debug: mostrar detalle del 422 u otros errores
        try:
            print("Response JSON:", response.json())
        except Exception:
            print("Response Text:", response.text)
    assert response.status_code == 201
    json_response = response.json()
    assert json_response["message"] == "Transmittal and documents uploaded successfully"


def test_create_ttal_np_doc_missing_fields(client, db_session):
    """Test de integración para crear un nuevo Ttal NP Doc con campos faltantes"""
    # No necesitamos reiniciar la DB aquí, el fixture db_session ya maneja la limpieza

    # Enviar solicitud con campos faltantes
    response = client.post(
        "/api/v1/ttal-docs/",
        files=[
            # Omito project_id para simular campo faltante
            ("ttal_np_code", (None, "TTALNP002")),
            (
                "ttal_np_description",
                (None, "Test Transmittal NP Document Missing Fields"),
            ),
            (
                "ttal_np_file",
                ("ttal_test.pdf", b"Test ttal file content", "application/pdf"),
            ),
            ("document_file", ("doc1.pdf", b"Test doc 1 content", "application/pdf")),
        ],
    )

    assert response.status_code == 422
    json_response = response.json()
    # Pydantic/FastAPI devuelve errores en detail como lista
    assert "detail" in json_response
    errors = json_response["detail"]
    assert isinstance(errors, list)
    # Verificar que al menos un error tenga msg "Field required"
    assert any(err.get("msg") == "Field required" for err in errors)


def test_create_ttal_exception(client, db_session):
    """Test de integración para crear un nuevo Ttal NP Doc que lanza excepción"""
    # Creo un proyecto de prueba con nombre único para evitar conflictos
    project_data = {
        "name": "Test Project Exception",
        "description": "A project for testing exceptions",
    }
    project = Project(
        nombre=project_data["name"],
        codigo="TP_EXCEPTION",
        descripcion=project_data["description"],
    )
    db_session.add(project)
    db_session.commit()
    db_session.refresh(project)
    # Primero creo un TTAL-NP con código específico para forzar excepción en segundo intento
    response_initial = client.post(
        "/api/v1/ttal-docs/",
        files=[
            ("project_id", (None, str(project.id))),
            ("ttal_np_code", (None, "TTALNP_EXCEPTION_01")),
            ("ttal_np_description", (None, "Test Transmittal NP Document")),
            # El endpoint actual toma el primer elemento y lo separa por comas
            ("document_code", (None, "DOC_EXC_001,DOC_EXC_002")),
            ("document_name", (None, "Document Exc 1,Document Exc 2")),
            ("document_revision", (None, "A,C")),
            # Archivos
            (
                "ttal_np_file",
                ("ttal_test.pdf", b"Test ttal file content", "application/pdf"),
            ),
            ("document_file", ("doc1.pdf", b"Test doc 1 content", "application/pdf")),
            ("document_file", ("doc2.pdf", b"Test doc 2 content", "application/pdf")),
        ],
    )
    assert response_initial.status_code == 201
    # Enviar solicitud que cause excepción (por ejemplo, código TTAL duplicado)
    response = client.post(
        "/api/v1/ttal-docs/",
        files=[
            ("project_id", (None, str(project.id))),
            ("ttal_np_code", (None, "TTALNP_EXCEPTION_01")),
            ("ttal_np_description", (None, "Test Transmittal NP Document")),
            # El endpoint actual toma el primer elemento y lo separa por comas
            ("document_code", (None, "DOC_EXC_001,DOC_EXC_002")),
            ("document_name", (None, "Document Exc 1,Document Exc 2")),
            ("document_revision", (None, "A,C")),
            # Archivos
            (
                "ttal_np_file",
                ("ttal_test.pdf", b"Test ttal file content", "application/pdf"),
            ),
            ("document_file", ("doc1.pdf", b"Test doc 1 content", "application/pdf")),
            ("document_file", ("doc2.pdf", b"Test doc 2 content", "application/pdf")),
        ],
    )

    assert response.status_code == 500
    json_response = response.json()
    assert "detail" in json_response
    assert json_response["detail"] == "Failed to create TTAL-NP record"
