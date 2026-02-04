"""Backward-compatible shim for transmittals routes.

This module re-exports the router from the new modular monolith layout
located in src.modules.transmittals.presentation.routes for backward compatibility.
"""
from src.modules.transmittals.presentation.routes import ttal_documents  # noqa: F401
