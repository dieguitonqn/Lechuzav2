import pytest
import sys
import os
from unittest.mock import MagicMock

# Agregar el directorio raíz del backend al Python path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))

from application.use_cases.company_uc import CompanyUseCase
from domain.entities.companies import Company


class TestCompanyUseCase:
    """Tests para el use case de creación de empresas"""

    @pytest.fixture
    def mock_company_repository(self):
        """Mock del repositorio de empresas"""
        return MagicMock()

    @pytest.fixture
    def use_case(self, mock_company_repository):
        """Instancia del use case con dependencias mockeadas"""
        return CompanyUseCase(company_repository=mock_company_repository)

    def test_create_company_success(self, use_case, mock_company_repository):
        """Test para la creación exitosa de una empresa"""
        # Arrange
        name = "Test Company"
        codigo = "TC001"

        # Crear una instancia mock de Company
        expected_company = Company(nombre=name, codigo=codigo)
        mock_company_repository.create_company.return_value = expected_company

        # Act
        result = use_case.create_company(name, codigo)

        # Assert
        assert result == expected_company
        assert result.nombre == name
        assert result.codigo == codigo
        mock_company_repository.create_company.assert_called_once_with(
            name=name, codigo=codigo
        )

    def test_create_company_repository_error(self, use_case, mock_company_repository):
        """Test para el caso de error en el repositorio"""
        # Arrange
        name = "Test Company"
        codigo = "TC001"

        mock_company_repository.create_company.side_effect = Exception("Database error")

        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            use_case.create_company(name, codigo)

        assert str(exc_info.value) == "Database error"
        mock_company_repository.create_company.assert_called_once_with(
            name=name, codigo=codigo
        )
