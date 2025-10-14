from fastapi import Depends, APIRouter, HTTPException, UploadFile, status, Form, File, UploadFile
from sqlmodel import Session
from typing import List
from api.v1.dependencies.get_proyect_uc import get_project_uc
from core.use_cases.projects_uc import ProjectUseCase
from core.dtos.projects_dto import ProjectCreateDTO
import uuid


projects = APIRouter(prefix="/projects")

@projects.post("/", status_code=status.HTTP_201_CREATED)
async def create_project(name: str=Form(...),
                         code: str=Form(...),
                         description: str=Form(...),
                         company_id: uuid.UUID = Form(...),
                         project_file: UploadFile = File(...),
                         project_uc: ProjectUseCase = Depends(get_project_uc)):

    project_dto: ProjectCreateDTO = ProjectCreateDTO(
        name=name,
        code=code,
        description=description,
        project_file=project_file,
        company_id=company_id

    )
    try:
        project = await project_uc.create_project(project_dto)
        return {"message": "Project created successfully", "project": project.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))