import pytest
from fastapi import status
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from presentation.api.v1.endpoints.companies import companies



@pytest.fixture
def client():
    """
    Cliente de prueba que usa la app principal para que los dependency overrides funcionen.
    """
    from main import app
    app.include_router(companies)  # Asegurarse que el router esté incluido
    
    with TestClient(app) as client:
        yield client

@pytest.fixture
def mock_company_uc():
    """
    Mockea la dependencia get_company_uc usada en el endpoint de companies.
    Devuelve un MagicMock con create_company configurado para retornar un diccionario simulado.
    """
    mocked_class = MagicMock()
    mocked_class.nombre = "TOTAL"
    mocked_class.codigo = "9876"
    mocked_class.id = "987654321-4321-4321-4321-123456789012"

    mock_uc = MagicMock()
    mock_uc.create_company.return_value = mocked_class
    return mock_uc

@pytest.fixture()
def ov_get_company_uc(mock_company_uc):
    """
    Override de la dependencia get_company_uc para usar el mock en los tests.
    """
    from presentation.api.v1.dependencies.get_company_uc import get_company_uc
    from main import app

    app.dependency_overrides[get_company_uc] = lambda: mock_company_uc
    try:
        yield mock_company_uc
    finally:
        app.dependency_overrides.pop(get_company_uc, None)

def test_create_company_success(client, ov_get_company_uc):
    """
    Test para la creación exitosa de una compañía.
    """
    response = client.post("/companies/", json={"name": "TOTAL", "code": "9876"})
    assert response.status_code == status.HTTP_201_CREATED
    
    # Verificar la respuesta
    response_data = response.json()
    assert response_data["message"] == "Company created successfully"
    assert response_data["name"] == "TOTAL"
    assert response_data["codigo"] == "9876"
    
    # Verificar que el mock fue llamado correctamente
    ov_get_company_uc.create_company.assert_called_once_with("TOTAL", "9876")

def test_create_company_failure(client, ov_get_company_uc):

    ov_get_company_uc.create_company.side_effect = Exception("Database error")

    response = client.post("/companies/", json={"name": "TOTAL", "code": "9876"})
    assert response.status_code == status.HTTP_400_BAD_REQUEST