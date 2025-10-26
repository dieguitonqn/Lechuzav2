from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
# from domain.entities.documents import Document  # Importa la clase Document para las relaciones


class Status(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(unique=True)
    descripcion: Optional[str] = None

    documents: List["Document"] = Relationship(back_populates="status")
