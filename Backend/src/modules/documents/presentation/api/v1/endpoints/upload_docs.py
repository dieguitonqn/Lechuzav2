from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response,
    status,
    Request,
)
from src.modules.documents.application.dtos import DocumentDTO
from src.modules.auth.presentation.api.v1.dependencies.get_current_user import (
    get_current_user,
)

# from src.modules.documents.presentation.api.v1. import get_document_uc
# from src.modules.documents.application.use_cases import DocumentUseCase

from src.domain.entities.users import User


upload_docs_router = APIRouter()


@upload_docs_router.post("/upload", status_code=status.HTTP_200_OK)
async def upload_documents(request: Request, user: User = Depends(get_current_user)):
    try:
        # Obtener todos los datos del form
        form = await request.form()

        # Extraer datos básicos
        obra_id = form.get("obra_id")
        obra_descripcion = form.get("obra_descripcion")
        np_ttal = form.get("np_ttal")
        np_ttal_descripcion = form.get("np_ttal_descripcion")
        np_ttal_file = form.get("np_ttal_file")

        # Validar campos obligatorios
        if not all(
            [obra_id, obra_descripcion, np_ttal, np_ttal_descripcion, np_ttal_file]
        ):
            missing_fields = []
            if not obra_id:
                missing_fields.append("obra_id")
            if not obra_descripcion:
                missing_fields.append("obra_descripcion")
            if not np_ttal:
                missing_fields.append("np_ttal")
            if not np_ttal_descripcion:
                missing_fields.append("np_ttal_descripcion")
            if not np_ttal_file:
                missing_fields.append("np_ttal_file")

            raise HTTPException(
                status_code=400,
                detail=f"Faltan campos obligatorios: {', '.join(missing_fields)}",
            )

        # Extraer documentos dinámicamente
        documentos = []
        i = 0
        while True:
            codigo_key = f"documentos[{i}][codigo]"
            revision_key = f"documentos[{i}][revision]"
            descripcion_key = f"documentos[{i}][descripcion]"
            file_key = f"documentos[{i}][file]"

            # Si no existe el código del documento i, terminar
            if codigo_key not in form:
                break

            codigo = form.get(codigo_key)
            revision = form.get(revision_key)
            descripcion = form.get(descripcion_key)
            file = form.get(file_key)

            # Validar que todos los campos del documento estén presentes
            if not all([codigo, revision, descripcion, file]):
                missing_doc_fields = []
                if not codigo:
                    missing_doc_fields.append("codigo")
                if not revision:
                    missing_doc_fields.append("revision")
                if not descripcion:
                    missing_doc_fields.append("descripcion")
                if not file:
                    missing_doc_fields.append("file")

                raise HTTPException(
                    status_code=400,
                    detail=f"Documento {i + 1} tiene campos faltantes: {', '.join(missing_doc_fields)}",
                )

            # Sanitizar nombre de archivo si existe
            if hasattr(file, 'filename') and file.filename:
                import re
                # Reemplazar caracteres problemáticos con guión bajo
                file.filename = re.sub(r'[^\w\-_\.]', '_', file.filename)
            
            documentos.append(
                DocumentDTO(
                    codigo=str(codigo) if codigo else "",
                    revision=str(revision) if revision else "",
                    descripcion=str(descripcion) if descripcion else "",
                    file=file
                )
            )
            i += 1

        # Validar que hay al menos un documento
        if not documentos:
            raise HTTPException(
                status_code=400, detail="Debe incluir al menos un documento"
            )

        # Sanitizar nombre del archivo transmittal
        if hasattr(np_ttal_file, 'filename') and np_ttal_file.filename:
            import re
            np_ttal_file.filename = re.sub(r'[^\w\-_\.]', '_', np_ttal_file.filename)
        
        # Crear el DTO principal
        # ingreso_dto = ingresoDocsDTO(
        #     obra_id=str(obra_id),
        #     obra_descripcion=str(obra_descripcion),
        #     np_ttal=str(np_ttal),
        #     np_ttal_file=np_ttal_file,
        #     np_ttal_descripcion=str(np_ttal_descripcion),
        #     documentos=documentos,
        # )

        # Aquí iría la lógica de negocio para procesar los documentos
        # return await document_uc.upload_documents(ingreso_dto, user)
        
        return Response(content="Documentos recibidos y procesados exitosamente", status_code=status.HTTP_200_OK)
    # {
    #         "message": "Documentos recibidos y procesados exitosamente",
    #         "obra_id": ingreso_dto.obra_id,
    #         "transmittal": ingreso_dto.np_ttal,
    #         "documentos_count": len(ingreso_dto.documentos),
    #         "user_id": str(user.id)
    #     }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error interno del servidor: {str(e)}"
        )
