import pytest
from unittest.mock import MagicMock

# Agregar el directorio raíz del backend al Python path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))

from application.use_cases.company_uc import CompanyUseCase
from domain.entities.companies import Company
from application.dtos.company_dto import CompanyDTO


@pytest.fixture
def mock_company_repository():
    """Mock del repositorio de empresas"""
    return MagicMock()

@pytest.fixture
def use_case(mock_company_repository):
    """Instancia del use case con dependencias mockeadas"""
    return CompanyUseCase(company_repository=mock_company_repository)

@pytest.fixture
def company_dto():
    return CompanyDTO(nombre="Test Company", codigo="TC001")

def test_create_company_success(use_case, mock_company_repository, company_dto):
    """Test para la creación exitosa de una empresa"""
    
    expected_company = Company(company_dto=company_dto)
    mock_company_repository.create_company.return_value = expected_company

    # Act
    result = use_case.create_company(company_dto)  # ← Llama al USE CASE, no al repositorio

    # Assert
    assert result == expected_company
    # Verificar que el repositorio fue llamado con los argumentos correctos
    mock_company_repository.create_company.assert_called_once_with(
        name=company_dto.nombre, codigo=company_dto.codigo  # ← Argumentos que espera el repositorio
    )

def test_create_company_repository_error(use_case, mock_company_repository, company_dto):
    """Test para el caso de error en el repositorio"""
    # Arrange
    mock_company_repository.create_company.side_effect = Exception("Database error")

    # Act & Assert
    with pytest.raises(Exception) as exc_info:
        use_case.create_company(company_dto)

    assert str(exc_info.value) == "Database error"
    mock_company_repository.create_company.assert_called_once_with(
        name=company_dto.nombre, codigo=company_dto.codigo  # ← Argumentos correctos
    )
