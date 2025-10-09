# 1. Importar todos los modelos (esto carga sus definiciones en el módulo 'models')

from models.users import User
from models.projects import Project

# 2. Re-exportar las clases para que puedan ser importadas desde `models`
__all__ = ["User", "Project"]

# 3. Resolver las referencias circulares *después* de que todos están cargados
# Llama a model_rebuild() en las clases que usan referencias forward (strings)

# En Pydantic v2 / SQLModel:
User.model_rebuild()
Project.model_rebuild()

# En Pydantic v1 (más antiguo):
# User.update_forward_refs()
# Team.update_forward_refs()