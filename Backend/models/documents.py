import uuid
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
# from models.projects import Project  # Importa la clase Project para las relaciones
from models.statuses import Status  # Importa la clase Status para las relaciones
from models.correction_reports import CorrectionReport  # Importa la clase CorrectionReport para las relaciones
from models.ttals_nps import Transmittal_NP  # Importa la clase Transmittal_NP para las relaciones


class Document(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    codigo: str
    nombre: str
    revision: str = Field(default="A")
    fecha_ingreso: datetime = Field(default_factory=datetime.now)
    fecha_vencimiento: Optional[datetime] = None
    document_file: str = Field(default="")  # Ruta o nombre del archivo asociado al documento
    
    # Relación a la tabla Status (Estado del documento)
    estado_id: int = Field(foreign_key="status.id")
    status: "Status" = Relationship(back_populates="documents")
    
    # Relación muchos a uno con CorrectionReport: varios documentos pueden compartir un mismo informe
    correction_report_id: Optional[uuid.UUID] = Field(default=None, foreign_key="correctionreport.id")
    correction_report: Optional["CorrectionReport"] = Relationship(back_populates="documents")
    

    # Relación de auto-referencia para documentos TTAL
    ttal_np_id: Optional[uuid.UUID] = Field(foreign_key="transmittal_np.id")
    ttal_np: Optional["Transmittal_NP"] = Relationship(back_populates="documents")

    # Relación con el proyecto al que pertenece
    project_id: uuid.UUID = Field(foreign_key="project.id")
    project: "Project" = Relationship(back_populates="documents")

from models.projects import Project