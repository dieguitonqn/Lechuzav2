from typing import List, Optional, TYPE_CHECKING
import uuid

from sqlmodel import Field, SQLModel, Relationship
from pydantic import BaseModel

if TYPE_CHECKING:
    from domain.entities.projects import Project
    from domain.entities.users import User


class Company(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    nombre: str = Field(unique=True)
    codigo: Optional[str] = Field(unique=True, default=None)
    # Relación a los proyectos a través de la tabla intermedia
    projects: Optional[List["Project"]] = Relationship(back_populates="companies")
    users: Optional[List["User"]] = Relationship(back_populates="company")


class CompanyEndpoint(BaseModel):
    name: str
    code: str
