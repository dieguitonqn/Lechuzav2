import pytest
import sys
import os
from unittest.mock import MagicMock

# Agregar el directorio raíz del backend al Python path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)

from application.use_cases.users_uc import CreateUserUseCase
from application.dtos.users_dto import UserCreateDTO


class TestCreateUserUseCase:
    """Tests para el use case de creación de usuarios"""

    @pytest.fixture
    def mock_user_repository(self):
        """Mock del repositorio de usuarios"""
        return MagicMock()

    @pytest.fixture
    def use_case(self, mock_user_repository):
        """Instancia del use case con dependencias mockeadas"""
        return CreateUserUseCase(user_repo=mock_user_repository)

    def test_execute_success(self, use_case, mock_user_repository):
        """Test para la creación exitosa de un usuario"""
        # Arrange
        user_dto = UserCreateDTO(email="test@example.com", password="password123")

        mock_user_repository.get_user_by_email.return_value = None  # Usuario no existe
        mock_user_repository.create_user.return_value = True  # Creación exitosa

        # Act
        result = use_case.execute(user_dto)

        # Assert
        assert result is True
        mock_user_repository.get_user_by_email.assert_called_once_with(user_dto.email)
        mock_user_repository.create_user.assert_called_once_with(
            user_dto.email, user_dto.password
        )

    def test_execute_missing_email(self, use_case, mock_user_repository):
        """Test para el caso de email faltante"""
        # Arrange
        invalid_dto = UserCreateDTO(
            email="",  # Email vacío
            password="password123",
        )

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            use_case.execute(invalid_dto)

        assert str(exc_info.value) == "Email and password are required"
