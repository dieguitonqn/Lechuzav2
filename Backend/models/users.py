import uuid
from datetime import datetime
from typing import Optional, List
from sqlalchemy import Column
from sqlalchemy.types import JSON

from sqlmodel import Field, SQLModel, Relationship
from models.companies import Company
from models.models_links import ProjectUserLink  # Importa la tabla intermedia para la relación muchos a muchos
from models.projects import Project  # Importa la clase Project para las relaciones


from pydantic import BaseModel

# Nueva tabla de relación para la lógica de permisos




# La tabla User se mantiene igual, ya que solo se relaciona con UNA empresa
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
    project_ids: Optional[List[uuid.UUID]] = Field(default=None, sa_column=Column(JSON))
    projects: Optional[List["Project"]] = Relationship(back_populates="users", link_model=ProjectUserLink)
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="company.id")
    company: Optional[Company] = Relationship(back_populates="users")


class UserCreate(BaseModel):
    email: str
    password: str
    is_active: bool = False
    is_epen_user: bool = False
    is_admin: bool = False



