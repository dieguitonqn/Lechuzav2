"""Backward-compatible shim for companies routes.

This module re-exports the router from the new modular monolith layout at
`src.modules.companies.presentation.routes` so existing imports keep working:

    from presentation.api.v1.endpoints.companies import companies

"""

from src.modules.companies.presentation.routes import router as companies  # type: ignore F401

