from fastapi import APIRouter
from src.modules.projects.presentation.api.v1.endpoints.new_project import new_project_router
from src.modules.projects.presentation.api.v1.endpoints.get_projects import get_projects_router

project_routers = APIRouter()
project_routers.include_router(new_project_router, prefix="/projects", tags=["projects"])
project_routers.include_router(get_projects_router, prefix="/projects", tags=["projects"])