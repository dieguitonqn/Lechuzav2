from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid


class DocumentBase(BaseModel):
    codigo: str
    nombre: str
    revision: str = Field(default="A")
    fecha_ingreso: datetime = Field(default_factory=datetime.now)
    fecha_vencimiento: Optional[datetime] = None
    document_file: str = Field(default="")  # Ruta o nombre del archivo asociado al documento
    estado_id: int
    correction_report_id: Optional[uuid.UUID] = None
    ttal_np_id: Optional[uuid.UUID] = None
    project_id: uuid.UUID
