from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException, status, Form, UploadFile, File
from typing import List
from sqlmodel import Session, select
import uuid
from models.ttals_nps import Transmittal_NP
from database.database import get_session


ttal_np = APIRouter( tags=["transmittal_np"])

@ttal_np.post("/ttal-nps", status_code=status.HTTP_201_CREATED)
async def create_ttal_np(
    project_id: str =Form(...),
    codigo: str=Form(...),
    asunto: str = Form(...),
    comentarios: str = Form(...),
    document_file: UploadFile = File(...),
    session: Session = Depends(get_session)):


    filename = Path(document_file.filename).name  # evita subdirectorios maliciosos en el nombre
    file_dir = Path("files") / project_id
    file_dir.mkdir(parents=True, exist_ok=True)
    file_location = file_dir / filename
    with open(file_location, "wb") as file_object:
        content = await document_file.read()
        file_object.write(content)

    
    new_ttal_np = Transmittal_NP(
        project_id=project_id,
        codigo=codigo,
        asunto=asunto,
        comentarios=comentarios,
        ttal_np_file=file_location
    )
    session.add(new_ttal_np)
    session.commit()
    session.refresh(new_ttal_np)
    return new_ttal_np