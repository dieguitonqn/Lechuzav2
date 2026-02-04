from fastapi import APIRouter, Depends, HTTPException, status, Form, File, UploadFile
from typing import Optional
import uuid
from src.modules.projects.presentation.dependencies import get_project_uc
from src.modules.projects.application.use_cases import ProjectUseCase
from src.modules.projects.application.dtos import ProjectCreateDTO
from src.modules.projects.domain.entities import Project


router = APIRouter(prefix="/projects")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_project(
    name: str = Form(...),
    code: str = Form(...),
    description: str = Form(...),
    company_id: uuid.UUID = Form(...),
    project_file: UploadFile = File(...),
    project_uc: ProjectUseCase = Depends(get_project_uc),
):
    project_dto: ProjectCreateDTO = ProjectCreateDTO(
        name=name,
        code=code,
        description=description,
        project_file=project_file,
        company_id=company_id,
    )
    try:
        project: Optional[Project] = await project_uc.create_project(project_dto)
        if project is None:
            raise HTTPException(status_code=500, detail="Failed to create project")
        return {"message": "Project created successfully", "project": project.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
