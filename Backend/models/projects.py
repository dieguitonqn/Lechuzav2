from typing import List, Optional
import uuid
from datetime import datetime
from fastapi import Form, UploadFile, File
from sqlalchemy import Column
from sqlalchemy.types import JSON
from sqlmodel import Field, SQLModel, Relationship
from models.models_links import ProjectUserLink  # Importa la clase User para las relaciones
from pydantic import BaseModel

from models.documents import Document  # Importa la clase Document para las relaciones
# from models.companies import Company  # Importa la clase Company para las relaciones


class Project(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    nombre: str = Field(unique=True)
    codigo: str = Field(unique=True)
    descripcion: Optional[str] = None
    fecha_inicio: datetime = Field(default_factory=datetime.now)
    fecha_fin: Optional[datetime] = None
    estado_proyecto: str = Field(default="Activo")
    emails_notificacion: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))    
    # Relación a los usuarios a través de la tabla intermedia
    users: List["User"] = Relationship(
        back_populates="projects", link_model=ProjectUserLink
    )
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="company.id")
    companies: List["Company"] = Relationship(back_populates="projects")
    documents: List["Document"] = Relationship(back_populates="project")
    contrato:Optional[str] = None
    contrato_url:Optional[str] = None


class ProjectCreate(BaseModel):
    name: str = Form(...)
    code: str = Form(...)
    description: Optional[str] = Form(None)
    emails_notification: Optional[List[str]] = Form(None)
    contract_file: UploadFile = File(...)
    contract: str = Form(None)

# from models.users import User
# from models.companies import Company