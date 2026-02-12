from fastapi import APIRouter


from src.modules.auth.presentation.api.v1 import auth_routers
from src.modules.projects.presentation.projects_routers import project_routers


module_routers = APIRouter()

# Include module routes
module_routers.include_router(auth_routers.auth_router)
module_routers.include_router(project_routers)