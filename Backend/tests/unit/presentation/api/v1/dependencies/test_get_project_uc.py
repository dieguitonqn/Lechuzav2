from unittest.mock import MagicMock
from presentation.api.v1.dependencies.get_proyect_uc import get_project_uc
from application.use_cases.projects_uc import ProjectUseCase



def test_get_project_use_case_dependency(monkeypatch):
    """Testea que la dependencia `get_project_use_case` retorne una instancia correcta de ProjectUseCase.

    Mockea la sesión de DB para evitar conexiones reales.
    """
    mock_session = MagicMock()

    # Patch get_session para que retorne el mock de sesión
    monkeypatch.setattr(
        "infrastructure.database.database.get_session",
        lambda: (yield mock_session),
        raising=False,
    )

    response = get_project_uc(session=mock_session)
    # Verifica que se haya creado una instancia de ProjectUseCase
    assert isinstance(response, ProjectUseCase)

