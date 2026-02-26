from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Request,
)
from src.modules.documents.application.dtos import RawUploadDataDTO
from src.modules.auth.presentation.api.v1.dependencies.get_current_user import (
    get_current_user,
)


from src.modules.documents.presentation.api.v1.dependencies.get_document_uc import get_document_uc
from src.modules.documents.application.uc_documents import DocumentsUC

from src.domain.entities.users import User


upload_docs_router = APIRouter()


@upload_docs_router.post("/upload", status_code=status.HTTP_200_OK)
async def upload_documents_ep(
    request: Request,
    user: User = Depends(get_current_user),
    document_uc: DocumentsUC = Depends(get_document_uc),
):
    """Endpoint para subir documentos. Solo maneja extracción básica de datos HTTP."""
    try:
        # Solo extraer datos raw del formulario
        form = await request.form()
        form_dict = {}
        
        # Convertir form a dict para facilitar el procesamiento
        for key in form.keys():
            form_dict[key] = form.get(key)
        
        raw_data = RawUploadDataDTO(form_data=form_dict)
        print (f"Datos raw recibidos: {raw_data.form_data}")
        
        # Delegar toda la validación y lógica de negocio al Use Case
        return await document_uc.upload_documents(raw_data, user)

        
    except HTTPException:
        raise
    except ValueError as e:
        # Errores de validación de negocio
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error interno del servidor: {str(e)}"
        )
