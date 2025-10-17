import pytest
from fastapi import status
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from api.v1.endpoints.companies import companies
from core.use_cases.company_uc import CompanyUseCase

# @pytest.fixture
# def client():
#     from main import app
#     app.include_router(companies)
#     return TestClient(app)

# @pytest.fixture
# def mock_company_uc(monkeypatch):
#     mock_uc = MagicMock()
#     monkeypatch.setattr("api.v1.endpoints.users.get_company_uc", lambda: mock_uc)
#     return mock_uc
@pytest.mark.skip("This test file is deprecated and will be removed in future versions.")
def test_create_company_success(client, mock_company_uc):
    mock_company_uc.create_company.return_value = {"name": "TOTAL", "codigo": "9876"}
    response = client.post("/companies/?name=TOTAL&codigo=9876")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"name": "TOTAL", "codigo": "9876"}
    mock_company_uc.create_company.assert_called_once_with("TOTAL", "9876")

@pytest.mark.skip("This test file is deprecated and will be removed in future versions.")
def test_create_company_error(client, mock_company_uc):
    mock_company_uc.create_company.side_effect = Exception("Error de prueba")
    response = client.post("/companies/?name=TOTAL&codigo=9876")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "Error de prueba"
