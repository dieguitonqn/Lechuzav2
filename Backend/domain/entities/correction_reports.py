from typing import List, Optional
import uuid
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.types import JSON
from sqlmodel import Field, Relationship, SQLModel


class CorrectionReport(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    document_id: List[uuid.UUID] = Field(default=None, sa_column=Column(JSON))
    fecha_correccion: datetime = Field(default_factory=datetime.now)
    comentarios: Optional[str] = None
    ruta_archivo_correccion: Optional[str] = None
    documents: List["Document"] = Relationship(back_populates="correction_report")