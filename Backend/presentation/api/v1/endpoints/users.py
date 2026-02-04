"""Backward-compatible shim for users routes.

This module re-exports the router from the new modular monolith layout at
`src.modules.users.presentation.routes` so existing imports keep working:

    from presentation.api.v1.endpoints.users import users

"""

from src.modules.users.presentation.routes import router as users  # noqa: F401
