# 1. Importar todos los modelos (esto carga sus definiciones en el módulo 'models')

from .users import User
from .projects import Project
from .companies import Company
from .documents import Document
from .statuses import Status
from .correction_reports import CorrectionReport
from .models_links import ProjectUserLink
from .ttals_nps import Transmittal_NP

# 2. Re-exportar las clases para que puedan ser importadas desde `models`
__all__ = [
    "User",
    "Project",
    "Company",
    "Document",
    "Status",
    "CorrectionReport",
    "ProjectUserLink",
    "Transmittal_NP",
]

# 3. Resolver las referencias circulares *después* de que todos están cargados
# Llama a model_rebuild() en las clases que usan referencias forward (strings)

# En Pydantic v2 / SQLModel:
User.model_rebuild()
Project.model_rebuild()
Company.model_rebuild()
Document.model_rebuild()
Status.model_rebuild()
CorrectionReport.model_rebuild()
Transmittal_NP.model_rebuild()
ProjectUserLink.model_rebuild()