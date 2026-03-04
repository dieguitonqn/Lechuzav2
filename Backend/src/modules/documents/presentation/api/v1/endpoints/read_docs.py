from fastapi import APIRouter, Depends, HTTPException, status

from src.modules.documents.application.uc_documents import DocumentsUC 
from src.modules.documents.presentation.api.v1.dependencies.get_document_uc import get_document_uc
from src.modules.auth.presentation.api.v1.dependencies.get_current_user import get_current_user
from src.domain.entities.users import User
from src.modules.documents.application.dtos import DocumentsResponse



read_docs_ep = APIRouter()


@read_docs_ep.get("/paginated_docs", response_model=DocumentsResponse, status_code=status.HTTP_200_OK)
async def read_all_docs(
        project_id: str,
        page: int = 1,
        page_size: int = 10,
        name_filter: str = None,
        code_filter: str = None,
        revision_filter: str = None,
        np_ttal_filter: str = None,
        status_filter: str = None,
        fecha_ingreso_filter: str = None,
        correction_report_filter: str = None,
        documents_uc: DocumentsUC = Depends(get_document_uc),
        user: User = Depends(get_current_user)
):
    """Obtiene documentos paginados de un proyecto."""
    print(f"El project_id recibido es: {project_id}")
    print(f"Parámetros de paginación: page={page}, page_size={page_size}")
    # ✅ VALIDAR Y CORREGIR PARÁMETROS
    page = max(1, page)  # Asegurar que page sea mínimo 1
    page_size = max(1, min(100, page_size))  # Entre 1 y 100
    try:
        # Obtener documentos y total directamente con page y page_size
        documents = await documents_uc.read_all_docs(
            project_id, page, page_size, name_filter, code_filter,
            revision_filter, np_ttal_filter, status_filter, fecha_ingreso_filter, correction_report_filter
        )
        total_documents = await documents_uc.get_total_documents_count(project_id)
        
        return {
            "documents": documents,
            "pagination": {
                "page": page,
                "page_size": page_size,
                "total": total_documents,
                "total_pages": (total_documents + page_size - 1) // page_size,
                "has_next": page * page_size < total_documents,
                "has_prev": page > 1
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")