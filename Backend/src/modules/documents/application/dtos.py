from fastapi import UploadFile
from typing import List
from dataclasses import dataclass

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
    np_ttal: str
    np_ttal_file: UploadFile
    np_ttal_descripcion: str
    documentos: List[DocumentDTO]