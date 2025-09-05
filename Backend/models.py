import uuid
from datetime import datetime
from typing import Optional, List
from sqlalchemy import Column
from sqlalchemy.types import JSON

from sqlmodel import Field, SQLModel, Relationship

# Nueva tabla de relación para la lógica de permisos
class ProjectCompanyLink(SQLModel, table=True):
    project_id: uuid.UUID = Field(
        foreign_key="project.id", primary_key=True
    )
    company_id: uuid.UUID = Field(
        foreign_key="company.id", primary_key=True
    )
    can_view_docs: bool = Field(default=False)
    can_upload_docs: bool = Field(default=False)
    can_correct_docs: bool = Field(default=False)

# Re-definición de la tabla Company
class Company(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    nombre: str = Field(unique=True)
    codigo: Optional[str] = Field(unique=True, default=None)
    # Relación a los proyectos a través de la tabla intermedia
    projects: List["Project"] = Relationship(
        back_populates="companies", link_model=ProjectCompanyLink
    )
    users: List["User"] = Relationship(back_populates="company")

# Re-definición de la tabla Project
class Project(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    nombre: str = Field(unique=True)
    codigo: str = Field(unique=True)
    descripcion: Optional[str] = None
    fecha_inicio: datetime
    fecha_fin: Optional[datetime] = None
    estado_proyecto: str = Field(default="Activo")
    emails_notificacion: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))    
    # Relación a las empresas a través de la tabla intermedia
    companies: List["Company"] = Relationship(
        back_populates="projects", link_model=ProjectCompanyLink
    )
    documents: List["Document"] = Relationship(back_populates="project")
    
# La tabla User se mantiene igual, ya que solo se relaciona con UNA empresa
class User(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(unique=True, index=True)
    password_hash: str
    nombre_completo: str
    is_epen_user: bool = Field(default=False)
    is_admin: bool = Field(default=False)
    is_active: bool = Field(default=True)
    fecha_creacion: datetime = Field(default_factory=datetime.now)
    password_reset_token: Optional[str] = None
    password_reset_expires: Optional[datetime] = None
    projets: List[Project] = Relationship(back_populates="users", link_model=ProjectCompanyLink)
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="company.id")
    company: Optional[Company] = Relationship(back_populates="users")

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
    correction_report: Optional["CorrectionReport"] = Relationship(
        back_populates="document"
    )

    # Relación de auto-referencia para documentos TTAL
    documento_ttal_adjunto_id: Optional[uuid.UUID] = Field(foreign_key="document.id")
    
    # Relación con el proyecto al que pertenece
    project: "Project" = Relationship(back_populates="documents")


class Status(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(unique=True)
    descripcion: Optional[str] = None
    
    documents: List["Document"] = Relationship(back_populates="status")
    