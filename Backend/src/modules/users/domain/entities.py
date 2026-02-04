"""Users domain entities - Re-exported from the original location.

For now, we re-export the original User entity to avoid table redefinition
errors in SQLAlchemy. Eventually, this module will own the entity definition.
"""

from domain.entities.users import User, UserCreate

__all__ = ["User", "UserCreate"]
