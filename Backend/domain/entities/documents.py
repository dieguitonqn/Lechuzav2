import uuid
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship

# Evitar importaciones en tiempo de ejecución que generen ciclos
if TYPE_CHECKING:
    from domain.entities.statuses import Status
    from domain.entities.correction_reports import CorrectionReport
    from domain.entities.ttals_nps import Transmittal_NP
    from domain.entities.projects import Project


class Document(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    codigo: str
    nombre: str
    revision: str = Field(default="A")
    fecha_ingreso: datetime = Field(default_factory=datetime.now)
    fecha_vencimiento: Optional[datetime] = None
    document_file: str = Field(
        default=""
    )  # Ruta o nombre del archivo asociado al documento

    # Relación a la tabla Status (Estado del documento)
    estado_id: int = Field(foreign_key="status.id")
    status: "Status" = Relationship(back_populates="documents")

    # Relación muchos a uno con CorrectionReport: varios documentos pueden compartir un mismo informe
    correction_report_id: Optional[uuid.UUID] = Field(
        default=None, foreign_key="correctionreport.id"
    )
    correction_report: Optional["CorrectionReport"] = Relationship(
        back_populates="documents"
    )

    # Relación de auto-referencia para documentos TTAL
    ttal_np_id: Optional[uuid.UUID] = Field(foreign_key="transmittal_np.id")
    ttal_np: Optional["Transmittal_NP"] = Relationship(back_populates="documents")

    # Relación con el proyecto al que pertenece
    project_id: uuid.UUID = Field(foreign_key="project.id", index=True)
    project: "Project" = Relationship(back_populates="documents")


# Nota: las importaciones de tipos relacionados se resuelven solo para comprobación de tipos
