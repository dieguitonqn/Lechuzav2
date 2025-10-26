from fastapi import APIRouter
from presentation.api.v1.endpoints import users, projects, ttal_np_documents, companies

router = APIRouter()

router.include_router(users.users)
# router.include_router(projects.router, prefix="/project", tags=["projects"])
router.include_router(ttal_np_documents.ttal_documents)
router.include_router(projects.projects)
router.include_router(companies.companies)
