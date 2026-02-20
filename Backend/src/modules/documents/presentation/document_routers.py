from fastapi import APIRouter, Depends, HTTPException, status, Header, Response
from typing import Optional, List
from src.modules.documents.presentation.api.v1.endpoints.upload_docs import upload_docs_router



document_routers = APIRouter(prefix="/documents")

document_routers.include_router(upload_docs_router)