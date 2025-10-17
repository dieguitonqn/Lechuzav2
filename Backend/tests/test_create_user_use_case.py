import pytest
from unittest.mock import MagicMock
from core.use_cases.users_uc import CreateUserUseCase
from core.dtos.users_dto import UserCreateDTO

# @pytest.fixture
# def user_repo():
#     repo = MagicMock()
#     repo.get_user_by_email.return_value = None
#     repo.create_user.return_value = MagicMock(email="test@example.com", password="hashedpass")
#     return repo

# @pytest.fixture
# def use_case(user_repo):
#     return CreateUserUseCase(user_repo)

@pytest.mark.skip("This test file is deprecated and will be removed in future versions.")
def test_create_user_success(use_case, user_repo):
    dto = UserCreateDTO(email="test@example.com", password="123456")
    user = use_case.execute(dto)
    assert user.email == "test@example.com"
    assert user.password == "hashedpass"
    user_repo.get_user_by_email.assert_called_once_with("test@example.com")
    user_repo.create_user.assert_called_once_with("test@example.com", "123456")

@pytest.mark.skip("This test file is deprecated and will be removed in future versions.")
def test_create_user_missing_email(use_case):
    dto = UserCreateDTO(email=None, password="123456")
    with pytest.raises(ValueError, match="Email and password are required"):
        use_case.execute(dto)

@pytest.mark.skip("This test file is deprecated and will be removed in future versions.")
def test_create_user_missing_password(use_case):
    dto = UserCreateDTO(email="test@example.com", password=None)
    with pytest.raises(ValueError, match="Email and password are required"):
        use_case.execute(dto)

@pytest.mark.skip("This test file is deprecated and will be removed in future versions.")
def test_create_user_already_exists(use_case, user_repo):
    user_repo.get_user_by_email.return_value = MagicMock(email="test@example.com")
    dto = UserCreateDTO(email="test@example.com", password="123456")
    with pytest.raises(ValueError, match="User with this email already exists"):
        use_case.execute(dto)
