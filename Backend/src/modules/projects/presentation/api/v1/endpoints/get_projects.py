from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.modules.projects.application.dtos import ProjectWithCompanies, CompanyDTO
from src.modules.projects.presentation.api.v1.dependencies import get_project_uc
from src.modules.projects.application.use_cases import ProjectUseCase
from src.domain.entities.projects import Project
from src.domain.entities.users import User
from src.modules.auth.presentation.api.v1.dependencies.get_current_user import get_current_user


get_projects_router = APIRouter()




@get_projects_router.get("/", response_model=List[ProjectWithCompanies])
async def get_projects(
    project_uc: ProjectUseCase = Depends(get_project_uc), 
    user: User = Depends(get_current_user)
):
    try:
        projects: List[Project] = project_uc.list_projects(user.id)
        response: List[ProjectWithCompanies] = []
        for project in projects:
            company_names = []
            if project.company is not None:
                company_names.append(project.company.nombre)

            response.append(
                ProjectWithCompanies(
                    id=str(project.id),
                    descripcion=project.descripcion,
                    fecha_fin=project.fecha_fin.isoformat() if project.fecha_fin else None,
                    emails_notificacion=project.emails_notificacion,
                    contrato=project.contrato,
                    nombre=project.nombre,
                    codigo=project.codigo,
                    card_color=project.card_color,
                    fecha_inicio=project.fecha_inicio.isoformat(),
                    estado_proyecto=project.estado_proyecto,
                    company_id=str(project.company_id) if project.company_id else None,
                    contrato_url=project.contrato_url,
                    companies=[CompanyDTO(id=str(project.company.id), nombre=project.company.nombre, codigo=project.company.codigo)] if project.company else None
                )
            )

        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))