from typing import List, Optional
import uuid
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.types import JSON
from sqlmodel import Field, SQLModel


    
class Transmittal_NP(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    project_id: uuid.UUID = Field(foreign_key="project.id")
    codigo: str
    fecha_emision: datetime = Field(default_factory=datetime.now)
    asunto: Optional[str] = None
    enviado_a: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))
    copias_a: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))
    comentarios: Optional[str] = None
    documents: Optional[List[uuid.UUID]] = Field(default=None, sa_column=Column(JSON))  # Lista de IDs de documentos