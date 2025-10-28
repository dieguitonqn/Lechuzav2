import pytest
from unittest.mock import MagicMock
from contextlib import asynccontextmanager


@pytest.fixture(autouse=True)
def disable_app_lifespan(monkeypatch):
    """Disable app lifespan DB initialization during tests.

    Replaces the FastAPI lifespan with a no-op so startup doesn't try to
    create tables or connect to the database. Keeps tests independent of DB.
    """
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
def mock_db_session(monkeypatch):
    """Mock the DB session dependency to avoid real DB connections.

    Patches infrastructure.database.database.get_session to yield a MagicMock
    session. Adjust targets if your code imports get_session into another module.
    """
    mock_session = MagicMock()

    def mock_get_session():
        yield mock_session

    # Parchea get_session en el módulo donde está definido
    monkeypatch.setattr(
        "infrastructure.database.database.get_session", mock_get_session, raising=True
    )

    return mock_session
