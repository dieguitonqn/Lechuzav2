"""Backward-compatible shim for projects routes.

This module re-exports the router from the new modular monolith layout at
`src.modules.projects.presentation.routes` so existing imports keep working:

    from presentation.api.v1.endpoints.projects import projects

"""

from src.modules.projects.presentation.routes import router as projects  # noqa: F401
