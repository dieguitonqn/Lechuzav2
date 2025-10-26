from typing import Optional
import uuid
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from domain.entities.documents import (
    Document,
)  # Importa la clase Document para las relaciones


class Transmittal_NP(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    project_id: uuid.UUID = Field(foreign_key="project.id")
    codigo: str = Field(unique=True, index=True)
    fecha_emision: datetime = Field(default_factory=datetime.now)
    asunto: Optional[str] = Field(default="")
    comentarios: Optional[str] = Field(default="")
    ttal_np_file: str = Field(
        default=""
    )  # Ruta o nombre del archivo asociado al TTAL-NP

    documents: Optional["Document"] = Relationship(back_populates="ttal_np")
