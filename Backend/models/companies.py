from typing import List, Optional
import uuid
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from models.projects import Project  # Importa la clase Project para las relaciones



class Company(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    nombre: str = Field(unique=True)
    codigo: Optional[str] = Field(unique=True, default=None)
    # Relación a los proyectos a través de la tabla intermedia
    projects: Optional[List["Project"]] = Relationship(back_populates="companies")
    users: Optional[List["User"]] = Relationship(back_populates="company")
