from fastapi import APIRouter
from api.v1.endpoints import users,projects, ttal_np_documents

router = APIRouter()

router.include_router(users.users, prefix="/user", tags=["users"])
# router.include_router(projects.router, prefix="/project", tags=["projects"])
router.include_router(ttal_np_documents.ttal_documents, prefix="/ttal-np", tags=["ttal-np"])    

