from datetime import datetime
import re
from typing import List
from pathlib import Path
from src.domain.entities.documents import Document
from src.domain.entities.users import User
from src.modules.documents.domain.interfaces import (
    IDocumentsRepository,
    IDocsFilesRepository,
    ITransmittalNPRepository,
)
from src.modules.documents.application.dtos import (
    DocumentToSaveFile,
    ingresoDocsDTO,
    RawUploadDataDTO,
    DocumentDTO,
    TtalNPDTO,
)
from src.domain.entities.ttals_nps import Transmittal_NP


class DocumentsUC:
    def __init__(
        self,
        document_repo: IDocumentsRepository,
        files_repo: IDocsFilesRepository,
        ttal_repo: ITransmittalNPRepository,
    ):
        self.document_repo = document_repo
        self.files_repo = files_repo
        self.ttal_repo = ttal_repo

    async def read_all_docs(
        self,
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
    ) -> List[Document]:
        """Obtiene documentos paginados de un proyecto específico."""
        try:
            # Validar parámetros de paginación
            if page < 1:
                page = 1
            if page_size < 1:
                page_size = 10
            if page_size > 100:  # Límite máximo para evitar sobrecarga
                page_size = 100

            # Calcular índices de paginación
            offset = (page - 1) * page_size
            print(f"Offset calculado: {offset}")  # Con page=1 debería ser 0, no -10
            limit = page_size

            # Obtener documentos paginados desde el repositorio
            documents = self.document_repo.get_documents_paginated(
                project_id=project_id,
                offset=offset,
                limit=limit,
                name_filter=name_filter,
                code_filter=code_filter,
                revision_filter=revision_filter,
                np_ttal_filter=np_ttal_filter,
                status_filter=status_filter,
                fecha_ingreso_filter=fecha_ingreso_filter,
                correction_report_filter=correction_report_filter,
            )

            return documents
        except Exception as e:
            raise Exception(f"Error al obtener documentos paginados: {str(e)}")

    async def get_total_documents_count(
        self, project_id: str) -> int:
        """Obtiene el total de documentos de un proyecto."""
        try:
            return self.document_repo.count_documents_by_project(
                project_id=str(project_id)
            )
        except Exception as e:
            raise Exception(f"Error al contar documentos: {str(e)}")

    async def upload_documents(self, raw_data: RawUploadDataDTO, user: User):
        """
        Procesa la subida de documentos con validación completa de reglas de negocio.
        Maneja toda la validación, sanitización y orquestación del proceso.
        """
        # Validar y procesar los datos raw
        ingreso_dto = await self._validate_and_process_raw_data(raw_data, user)

        # Procesar los documentos validados
        return await self._process_validated_documents(ingreso_dto, user)

    async def _validate_and_process_raw_data(
        self, raw_data: RawUploadDataDTO, user: User
    ) -> ingresoDocsDTO:
        """Valida y transforma los datos raw del formulario en un DTO válido."""
        form = raw_data.form_data

        # Extraer datos básicos
        obra_id = form.get("obra_id")
        obra_descripcion = form.get("obra_descripcion")
        obra_slug = form.get("obra_codigo")
        np_ttal = form.get("np_ttal")
        np_ttal_descripcion = form.get("np_ttal_descripcion")
        np_ttal_file = form.get("np_ttal_file")

        # Validar campos obligatorios
        self._validate_required_fields(
            obra_id,
            obra_descripcion,
            obra_slug,
            np_ttal,
            np_ttal_descripcion,
            np_ttal_file,
        )

        # Extraer y validar documentos
        documentos = self._extract_and_validate_documents(form)

        # Sanitizar archivos
        self._sanitize_file_names(np_ttal_file, documentos)

        return ingresoDocsDTO(
            obra_id=str(obra_id),
            obra_descripcion=str(obra_descripcion),
            obra_slug=str(obra_slug),
            np_ttal=str(np_ttal),
            np_ttal_file=np_ttal_file,
            np_ttal_descripcion=str(np_ttal_descripcion),
            documentos=documentos,
            user=user,
        )

    def _validate_required_fields(
        self,
        obra_id,
        obra_descripcion,
        obra_slug,
        np_ttal,
        np_ttal_descripcion,
        np_ttal_file,
    ):
        """Valida que todos los campos obligatorios estén presentes."""
        missing_fields = []

        if not obra_id:
            missing_fields.append("obra_id")
        if not obra_descripcion:
            missing_fields.append("obra_descripcion")
        if not obra_slug:
            missing_fields.append("obra_slug")
        if not np_ttal:
            missing_fields.append("np_ttal")
        if not np_ttal_descripcion:
            missing_fields.append("np_ttal_descripcion")
        if not np_ttal_file:
            missing_fields.append("np_ttal_file")

        if missing_fields:
            raise ValueError(f"Faltan campos obligatorios: {', '.join(missing_fields)}")

    def _extract_and_validate_documents(self, form) -> List[DocumentDTO]:
        """Extrae y valida los documentos dinámicamente del formulario."""
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

            # Validar campos del documento
            self._validate_document_fields(codigo, revision, descripcion, file, i + 1)

            documentos.append(
                DocumentDTO(
                    codigo=str(codigo) if codigo else "",
                    revision=str(revision) if revision else "",
                    descripcion=str(descripcion) if descripcion else "",
                    file=file,
                )
            )
            i += 1

        # Validar que hay al menos un documento
        if not documentos:
            raise ValueError("Debe incluir al menos un documento")

        return documentos

    def _validate_document_fields(
        self, codigo, revision, descripcion, file, doc_number
    ):
        """Valida los campos de un documento específico."""
        missing_fields = []

        if not codigo:
            missing_fields.append("codigo")
        if not revision:
            missing_fields.append("revision")
        if not descripcion:
            missing_fields.append("descripcion")
        if not file:
            missing_fields.append("file")

        if missing_fields:
            raise ValueError(
                f"Documento {doc_number} tiene campos faltantes: {', '.join(missing_fields)}"
            )

    def _sanitize_file_names(self, np_ttal_file, documentos: List[DocumentDTO]):
        """Sanitiza los nombres de archivos para evitar problemas de sistema."""
        # Sanitizar archivo transmittal
        if hasattr(np_ttal_file, "filename") and np_ttal_file.filename:
            np_ttal_file.filename = re.sub(r"[^\w\-_\.]", "_", np_ttal_file.filename)

        # Sanitizar archivos de documentos
        for doc in documentos:
            if hasattr(doc.file, "filename") and doc.file.filename:
                doc.file.filename = re.sub(r"[^\w\-_\.]", "_", doc.file.filename)

    async def _process_validated_documents(
        self, ingreso_dto: ingresoDocsDTO, user: User
    ):
        """Procesa los documentos ya validados, guardándolos en el sistema."""
        sliced_uuid = ingreso_dto.obra_id[:8]
        # Aquí deberías implementar la lógica real para guardar el archivo, por ejemplo:
        dir_path = Path("storage") / f"{ingreso_dto.obra_slug}-{sliced_uuid}"

        # Guardar el archivo transmittal
        ttal_np_dto = TtalNPDTO(
            np_ttal=ingreso_dto.np_ttal,
            np_ttal_descripcion=ingreso_dto.np_ttal_descripcion,
            np_ttal_file=ingreso_dto.np_ttal_file,
            obra_id=ingreso_dto.obra_id,
            obra_slug=ingreso_dto.obra_slug,
        )
        np_ttal_file_path: str = await self.ttal_repo.save_transmittal_np_file(
            ttal_dto=ttal_np_dto, user=user, dirpath=dir_path
        )

        # Crear y guardar el transmittal en base de datos
        new_ttal_np = Transmittal_NP(
            project_id=ingreso_dto.obra_id,
            codigo=ingreso_dto.np_ttal,
            asunto=ingreso_dto.np_ttal_descripcion,
            ttal_np_file=np_ttal_file_path,
        )
        ttal_np_id = await self.ttal_repo.save_transmittal_np_toDB(new_ttal_np, user)

        # Procesar cada documento
        processed_docs = []
        for doc in ingreso_dto.documentos:
            # Guardar archivo del documento
            document_to_save = DocumentToSaveFile(
                codigo=doc.codigo,
                revision=doc.revision,
                descripcion=doc.descripcion,
                file=doc.file,
                obra_id=ingreso_dto.obra_id,
                obra_slug=ingreso_dto.obra_slug,
            )
            file_path = await self.files_repo.save_file(
                document_to_save, user, dirpath=dir_path
            )

            # Crear entidad documento para base de datos
            document_toDB = Document(
                codigo=doc.codigo,
                nombre=doc.descripcion,
                fecha_ingreso=datetime.now(),
                revision=doc.revision,
                document_file=file_path,
                project_id=ingreso_dto.obra_id,
                estado_id=int(1),
                ttal_np_id=ttal_np_id,
            )

            # Guardar documento en base de datos
            document_saved: Document = self.document_repo.save_document_toDB(
                document_toDB, user
            )

            print(f"Documento guardado en DB: {document_saved}")

            processed_docs.append(
                {
                    "codigo": doc.codigo,
                    "revision": doc.revision,
                    "descripcion": doc.descripcion,
                }
            )
        print(f"Documentos procesados: {processed_docs}")
        # Retornar resumen del procesamiento
        return {
            "message": "Documentos procesados exitosamente",
            "obra_id": ingreso_dto.obra_id,
            "transmittal": ingreso_dto.np_ttal,
            "documentos_count": len(processed_docs),
            "documentos_procesados": processed_docs,
            "user_id": str(user.id),
        }
