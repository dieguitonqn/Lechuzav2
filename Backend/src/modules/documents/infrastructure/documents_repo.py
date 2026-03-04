import uuid

from src.domain.entities.documents import Document
from src.modules.documents.domain.interfaces import IDocumentsRepository
from sqlmodel import Session, select, col, func


class DocumentsRepository(IDocumentsRepository):
    def __init__(self, session: Session):
        # Inicializar con la sesión recibida como parámetro
        self.session = session

    def save_document_toDB(self, document: Document, user):
        # Aquí iría la lógica para guardar los documentos en la base de datos
        existing_doc = self.session.exec(
            select(Document).where(
                Document.codigo == document.codigo,
                Document.revision == document.revision,
                Document.project_id == document.project_id,
            )
        ).first()

        if existing_doc:
            raise Exception(
                f"El documento con código {document.codigo} y revisión {document.revision} ya existe para el proyecto {document.project_id}"
            )
        try:
            self.session.add(document)
            self.session.commit()

            # Recargar el documento para obtener valores generados (ID, timestamps, etc.)
            self.session.refresh(document)

            # Ahora retornar el documento actualizado
            return document
        except Exception as e:
            self.session.rollback()
            raise e

    def get_documents_paginated(
        self,
        project_id: str,
        offset: int = 0,
        limit: int = 10,
        name_filter: str = None,
        code_filter: str = None,
        revision_filter: str = None,
        np_ttal_filter: str = None,
        status_filter: str = None,
        fecha_ingreso_filter: str = None,
        correction_report_filter: str = None,
    ) -> list[Document]:
        try:
            # Validar UUID temprano para mejor error handling
            project_uuid = uuid.UUID(project_id)

            query = select(Document).where(Document.project_id == project_uuid)

            # Aplicar filtros - usando los nombres REALES de los campos de la BD
            if name_filter:
                query = query.where(col(Document.nombre).contains(name_filter))
            if code_filter:
                query = query.where(col(Document.codigo).contains(code_filter))
            if revision_filter:
                query = query.where(col(Document.revision).contains(revision_filter))
            # ✅ CORREGIR: usar ttal_np_id en lugar de np_ttal
            if np_ttal_filter:
                query = query.where(col(Document.ttal_np_id).ilike(f"%{np_ttal_filter}%"))
            # ✅ CORREGIR: usar estado_id en lugar de status  
            if status_filter:
                query = query.where(col(Document.estado_id).ilike(f"%{status_filter}%"))
            if fecha_ingreso_filter:
                query = query.where(col(Document.fecha_ingreso).contains(fecha_ingreso_filter))
            # ✅ CORREGIR: usar correction_report_id en lugar de correction_report
            if correction_report_filter:
                query = query.where(col(Document.correction_report_id).ilike(f"%{correction_report_filter}%"))

            return self.session.exec(query.offset(offset).limit(limit)).all()
        except ValueError as e:
            raise Exception(f"project_id inválido: {str(e)}")
        except Exception as e:
            raise Exception(f"Error al obtener documentos paginados: {str(e)}")

    def count_documents_by_project(self, project_id: str) -> int:
        try:
            project_id = uuid.UUID(project_id)
            return self.session.exec(
                select(func.count()).where(Document.project_id == project_id)
            ).one()
        except Exception as e:
            raise Exception(f"Error al contar documentos por proyecto: {str(e)}")
