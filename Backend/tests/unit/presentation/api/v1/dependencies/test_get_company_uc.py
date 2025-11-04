from unittest.mock import MagicMock
from presentation.api.v1.dependencies.get_company_uc import get_company_uc
from application.use_cases.company_uc import CompanyUseCase


def test_get_company_use_case_dependency(monkeypatch):
    """Testea que la dependencia `get_company_use_case` retorne una instancia correcta de CompanyUseCase.

    Mockea la sesión de DB para evitar conexiones reales.
    """
    mock_session = MagicMock()

    # Patch get_session para que retorne el mock de sesión
    monkeypatch.setattr(
        "infrastructure.database.database.get_session",
        lambda: (yield mock_session),
        raising=False,
    )

    response = get_company_uc(session=mock_session)
    # Verifica que se haya creado una instancia de CompanyUseCase
    assert isinstance(response, CompanyUseCase)