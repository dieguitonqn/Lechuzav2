from fastapi import APIRouter, Depends


from src.modules.auth.presentation.api.v1 import auth_routers


module_routers = APIRouter()

# Include module routes
module_routers.include_router(auth_routers.auth_router)