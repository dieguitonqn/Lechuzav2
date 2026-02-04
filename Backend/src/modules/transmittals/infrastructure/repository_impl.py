from sqlmodel import Session
from src.modules.transmittals.domain.repositories import ITtalNpRepository, IDocumentRepository
from infrastructure.database.database import get_session
from src.modules.transmittals.domain.entities import Transmittal_NP, Document


class SQLModelTtalNpRepository(ITtalNpRepository):
    def __init__(self, session: Session = get_session()):
        self.session = session

    def create_ttal_np(
        self, project_id: str, codigo: str, asunto: str, ttal_np_file: str
    ):
        ttal_np_db = Transmittal_NP(
            project_id=project_id,
            codigo=codigo,
            asunto=asunto,
            ttal_np_file=ttal_np_file,
        )
        try:
            self.session.add(ttal_np_db)
            self.session.commit()
            self.session.refresh(ttal_np_db)
            return ttal_np_db
        except Exception as e:
            print(f"Error creating TTAL-NP: {e}")
            self.session.rollback()
            return None


class SQLModelDocumentRepository(IDocumentRepository):
    def __init__(self, session: Session = get_session()):
        self.session = session

    def create_document(
        self,
        codigo: str,
        nombre: str,
        revision: str,
        document_file: str,
        project_id: str = "",
        ttal_np_id: str = "",
    ):
        document_db = Document(
            codigo=codigo,
            nombre=nombre,
            revision=revision,
            document_file=document_file,
            project_id=project_id,
            ttal_np_id=ttal_np_id,
            estado_id=1,  # Asignar un estado por defecto (por ejemplo, "Nuevo" con id=1
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
