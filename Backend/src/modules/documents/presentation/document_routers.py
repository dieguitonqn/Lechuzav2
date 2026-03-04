from fastapi import APIRouter
from src.modules.documents.presentation.api.v1.endpoints.upload_docs import upload_docs_router
from src.modules.documents.presentation.api.v1.endpoints.read_docs import read_docs_ep


document_routers = APIRouter(prefix="/documents")

document_routers.include_router(upload_docs_router)
document_routers.include_router(read_docs_ep)