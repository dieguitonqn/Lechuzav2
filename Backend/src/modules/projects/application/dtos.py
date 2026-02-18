from fastapi import UploadFile
import uuid
from typing import List, Optional
from pydantic import BaseModel



class ProjectCreateDTO:
    def __init__(
        self,
        name: str,
        code: str,
        description: str,
        project_file: UploadFile,
        company_id: uuid.UUID,
    ):
        self.name = name
        self.description = description
        self.code = code
        self.project_file = project_file
        self.company_id = company_id
class ProjectDTO:
    def __init__(
        self,
        id: str,
        name: str,
        code: str,
        description: str,
        project_file: str,
        company_id: str,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.code = code
        self.project_file = project_file
        self.company_id = company_id

class CompanyDTO(BaseModel):
    id: str
    nombre: str
    codigo: Optional[str] = None
   
class ProjectWithCompanies(BaseModel):
    id: str
    descripcion: Optional[str] = None
    fecha_fin: Optional[str] = None
    emails_notificacion: Optional[List[str]] = None
    contrato: Optional[str] = None
    nombre: str
    codigo: str
    card_color: Optional[str] = None
    fecha_inicio: str
    estado_proyecto: str
    company_id: Optional[str] = None
    contrato_url: Optional[str] = None
    companies: Optional[List[CompanyDTO]] = None