import uuid
from sqlmodel import Session
from core.interfaces.documents import IDocumentRepository
from database.database import get_session
from models.documents import Document

class SQLModelDocumentRepository(IDocumentRepository):

    def __init__(self, session: Session = get_session()):
        self.session = session

    def create_document(self, codigo: str, 
                              nombre: str, 
                              revision: str, 
                              document_file: str, 
                              project_id: str,
                              ttal_np_id: uuid.UUID = None):
        document_db = Document(
            codigo=codigo,
            nombre=nombre,
            revision=revision,
            document_file=document_file,
            project_id=project_id,
            ttal_np_id=ttal_np_id,
            estado_id=1  # Asignar un estado por defecto (por ejemplo, "Nuevo" con id=1
        )
        try:
            self.session.add(document_db)
            self.session.commit()
            self.session.refresh(document_db)
            return document_db
        except Exception as e:
            print(f"Error creating Document: {e}")
            self.session.rollback()
            return None