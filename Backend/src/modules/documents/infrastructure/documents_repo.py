
from src.domain.entities.documents import Document
from src.modules.documents.domain.interfaces import IDocumentsRepository
from sqlmodel import Session, select


class DocumentsRepository(IDocumentsRepository):
    def __init__(self, session: Session):
        # Inicializar con la sesión recibida como parámetro
        self.session = session

    def save_document_toDB(self, document: Document, user):
        # Aquí iría la lógica para guardar los documentos en la base de datos
        existing_doc = self.session.exec(select(Document).where(
            Document.codigo == document.codigo,
            Document.revision == document.revision,
            Document.project_id == document.project_id
        )).first()
        
        if existing_doc:
            raise Exception(f"El documento con código {document.codigo} y revisión {document.revision} ya existe para el proyecto {document.project_id}")
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
        