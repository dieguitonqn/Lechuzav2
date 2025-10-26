# 1. Importar todos los modelos (esto carga sus definiciones en el módulo 'models')

from domain.entities.users import User
from domain.entities.projects import Project
from domain.entities.companies import Company
from domain.entities.documents import Document
from domain.entities.statuses import Status
from domain.entities.correction_reports import CorrectionReport
from domain.entities.models_links import ProjectUserLink
from domain.entities.ttals_nps import Transmittal_NP

# 2. Re-exportar las clases para que puedan ser importadas desde `models`
__all__ = ["User", "Project", "Company", "Document", "Status", "CorrectionReport", "ProjectUserLink", "Transmittal_NP"]

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


# En Pydantic v1 (más antiguo):
# User.update_forward_refs()
# Team.update_forward_refs()
