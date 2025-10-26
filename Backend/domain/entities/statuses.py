from typing import List, Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship

# Evitar importaciones en tiempo de ejecución que generen ciclos
if TYPE_CHECKING:
    from domain.entities.documents import Document


class Status(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(unique=True)
    descripcion: Optional[str] = None

    documents: List["Document"] = Relationship(back_populates="status")
