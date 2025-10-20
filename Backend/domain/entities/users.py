import uuid
from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from domain.entities.companies import Company
from domain.entities.models_links import ProjectUserLink  # Importa la tabla intermedia para la relación muchos a muchos
from domain.entities.projects import Project  # Importa la clase Project para las relaciones


from pydantic import BaseModel

# Nueva tabla de relación para la lógica de permisos


class User(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(unique=True, index=True)
    password_hash: str
    nombre_completo: Optional[str] = None
    is_epen_user: bool = Field(default=False)
    is_admin: bool = Field(default=False)
    is_active: bool = Field(default=False)
    fecha_creacion: datetime = Field(default_factory=datetime.now)
    password_reset_token: Optional[str] = None
    password_reset_expires: Optional[datetime] = None
    
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="company.id")
    company: Optional[Company] = Relationship(back_populates="users")
# Relación a los proyectos a través de la tabla intermedia. Como es de muchos a muchos, es una lista y no tiene foreign_key
    projects: Optional[List["Project"]] = Relationship(back_populates="users", link_model=ProjectUserLink)


class UserCreate(BaseModel):
    email: str
    password: str
    is_active: bool = False
    is_epen_user: bool = False
    is_admin: bool = False



