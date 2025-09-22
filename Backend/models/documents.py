import uuid
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
# from models.projects import Project  # Importa la clase Project para las relaciones
from models.statuses import Status  # Importa la clase Status para las relaciones
from models.correction_reports import CorrectionReport  # Importa la clase CorrectionReport para las relaciones


class Document(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    project_id: uuid.UUID = Field(foreign_key="project.id")
    codigo: str
    nombre: str
    revision: str = Field(default="A")
    ruta_archivo: str
    fecha_ingreso: datetime = Field(default_factory=datetime.now)
    fecha_vencimiento: Optional[datetime] = None
    
    # Relación a la tabla Status (Estado del documento)
    estado_id: int = Field(foreign_key="status.id")
    status: "Status" = Relationship(back_populates="documents")
    
    # Relación con el informe de corrección (uno a uno)
    correction_report: Optional[uuid.UUID] = Field(default=None, foreign_key="correctionreport.id", unique=True)
    

    # Relación de auto-referencia para documentos TTAL
    documento_ttal_adjunto_id: Optional[uuid.UUID] = Field(foreign_key="document.id")
    
    # Relación con el proyecto al que pertenece
    project: "Project" = Relationship(back_populates="documents")