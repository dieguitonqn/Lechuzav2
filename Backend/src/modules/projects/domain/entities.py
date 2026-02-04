"""Projects domain entities - Re-exported from the original location.

For now, we re-export the original Project entity to avoid table redefinition
errors in SQLAlchemy. Eventually, this module will own the entity definition.
"""

from domain.entities.projects import Project, ProjectCreate

__all__ = ["Project", "ProjectCreate"]
