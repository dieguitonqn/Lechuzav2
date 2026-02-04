"""Transmittals domain entities - Re-exported from the original location.

For now, we re-export the original entities to avoid table redefinition
errors in SQLAlchemy. Eventually, this module will own the entity definitions.
"""

from domain.entities.ttals_nps import Transmittal_NP
from domain.entities.documents import Document

__all__ = ["Transmittal_NP", "Document"]
