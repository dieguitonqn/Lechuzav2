from fastapi import UploadFile
from typing import List, Any, Dict
from dataclasses import dataclass

from pydantic import BaseModel
from src.domain.entities.documents import Document
from src.domain.entities.users import User

@dataclass
class RawUploadDataDTO:
    """DTO para datos raw extraídos del formulario HTTP"""
    form_data: Dict[str, Any]

@dataclass
class DocumentDTO:
    codigo: str
    revision: str
    descripcion: str
    file: UploadFile

@dataclass
class ingresoDocsDTO:
    obra_id: str
    obra_descripcion: str
    obra_slug: str
    np_ttal: str
    user: User
    np_ttal_file: UploadFile
    np_ttal_descripcion: str
    documentos: List[DocumentDTO]

@dataclass
class TtalNPDTO:
    np_ttal: str
    np_ttal_descripcion: str
    np_ttal_file: UploadFile
    obra_id: str
    obra_slug: str

@dataclass
class DocumentToSaveFile:
    codigo: str
    revision: str
    descripcion: str
    file: UploadFile
    obra_id: str
    obra_slug: str

class PaginationInfo(BaseModel):
    page: int
    page_size: int
    total: int
    total_pages: int
    has_next: bool
    has_prev: bool


class DocumentsResponse(BaseModel):
    documents: list[Document]
    pagination: PaginationInfo
