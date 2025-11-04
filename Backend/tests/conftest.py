import pytest
from unittest.mock import MagicMock
from contextlib import asynccontextmanager


def _is_unit_test(request):
    """Check if the current test is a unit test based on its path."""
    return "unit" in str(request.fspath)


@pytest.fixture(autouse=True)
def disable_app_lifespan(monkeypatch, request):
    """Disable app lifespan DB initialization during unit tests only.

    Replaces the FastAPI lifespan with a no-op so startup doesn't try to
    create tables or connect to the database. Keeps tests independent of DB.
    Only applies to unit tests.
    """
    if not _is_unit_test(request):
        return  # Skip for integration/e2e tests

    try:
        import main

        @asynccontextmanager
        async def _noop(_app):
            yield

        # Replace the app's lifespan context to avoid DB setup
        if hasattr(main, "app") and hasattr(main.app, "router"):
            main.app.router.lifespan_context = _noop

        # Also ensure create_db_and_tables is a no-op if called somewhere
        monkeypatch.setattr("main.create_db_and_tables", lambda: None, raising=False)
        monkeypatch.setattr(
            "infrastructure.database.database.create_db_and_tables",
            lambda: None,
            raising=False,
        )
    except Exception:
        # If import main fails in some test suites, just skip silently
        pass


@pytest.fixture(autouse=True)
def mock_db_session(monkeypatch, request):
    """Mock the DB session dependency to avoid real DB connections in unit tests.

    Patches infrastructure.database.database.get_session to yield a MagicMock
    session. Adjust targets if your code imports get_session into another module.
    Only applies to unit tests.
    """
    if not _is_unit_test(request):
        return  # Skip for integration/e2e tests

    mock_session = MagicMock()

    def mock_get_session():
        yield mock_session

    # Parchea get_session en el módulo donde está definido
    monkeypatch.setattr(
        "infrastructure.database.database.get_session", mock_get_session, raising=True
    )

    return mock_session
