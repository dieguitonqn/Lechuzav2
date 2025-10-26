import pytest
from fastapi.testclient import TestClient
from fastapi import status
from unittest.mock import MagicMock, ANY
from main import app
from presentation.api.v1.endpoints.users import users
from presentation.api.v1.dependencies.get_user_create import get_user_create_use_case

# Incluir el router en la app para los tests
app.include_router(users)


@pytest.fixture
def client():
    """
    Cliente de prueba para simular peticiones HTTP.
    """
    with TestClient(app) as c:
        yield c


@pytest.fixture
def mock_create_user_use_case():
    """Mockea la dependencia `get_user_create_use_case` usando app.dependency_overrides.

    Devuelve un MagicMock con `execute` configurado para retornar un objeto `User`.
    """
    mock_uc = MagicMock()
    # mock_user = User(
    #     id=uuid.uuid4(),
    #     email="test@example.com",
    #     password_hash="hashedpassword123",
    #     is_active=False,
    #     is_epen_user=False,
    #     is_admin=False,
    # )
    mock_uc.execute.return_value = True

    # Override the dependency used by FastAPI
    app.dependency_overrides[get_user_create_use_case] = lambda: mock_uc

    try:
        yield mock_uc
    finally:
        # Clean up override after test
        app.dependency_overrides.pop(get_user_create_use_case, None)


def test_create_user_success(client, mock_create_user_use_case):
    """
    Test para la creación exitosa de un usuario.
    """
    # El mock ya está configurado para devolver un User en el fixture
    response = client.post(
        "/users/", data={"email": "test@example.com", "password": "password123"}
    )

    # Verifica el resultado
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"message": "User created successfully"}
    # Verifica que execute fue llamado con los datos correctos
    mock_create_user_use_case.execute.assert_called_once_with(ANY)
    # Verifica que el objeto devuelto por execute es un User
    assert isinstance(mock_create_user_use_case.execute.return_value, bool)
    assert mock_create_user_use_case.execute.return_value is True


def test_create_user_error(client, mock_create_user_use_case):
    """
    Test para el caso de error (ej: email duplicado).
    """
    mock_create_user_use_case.execute.side_effect = ValueError(
        "User with this email already exists"
    )
    response = client.post(
        "/users/", data={"email": "test@example.com", "password": "password123"}
    )

    # Verifica el resultado
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "User with this email already exists"}
