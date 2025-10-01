from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlmodel import Session, select
from typing import List
import uuid
from models.documents import Document
from database import get_session
from pathlib import Path


documents = APIRouter( tags=["documents"])

@documents.post("/documents", response_model=Document)
async def create_document(
    codigo: str = Form(...), 
    nombre: str = Form(...), 
    revision: str = Form(...), 
    estado_id: str = Form(...), 
    project_id: str = Form(...),
    document_file:UploadFile = File(...),
    session: Session = Depends(get_session)
    ):

    filename = Path(document_file.filename).name  # evita subdirectorios maliciosos en el nombre
    file_dir = Path("files") / project_id
    file_dir.mkdir(parents=True, exist_ok=True)
    file_location = file_dir / filename
    with open(file_location, "wb") as file_object:
        content = await document_file.read()
        file_object.write(content)
    
    new_doc = Document(
        codigo=codigo,
        nombre=nombre,
        revision=revision,
        estado_id=estado_id,
        project_id=project_id,
        document_file=file_location
    )
    session.add(new_doc)
    session.commit()
    session.refresh(new_doc)
    return new_doc


@documents.get("/documents")
async def read_documents(session: Session = Depends(get_session)):
    documents = session.exec(select(Document)).all()
    document=documents[0]
    return documents, document, document.project, document.status, document.correction_report, document.ttal_np