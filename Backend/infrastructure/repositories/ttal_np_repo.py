from domain.interfaces.ttal_np import ITtalNpRepository
from infrastructure.database.database import get_session
from sqlmodel import Session
from domain.entities.ttals_nps import Transmittal_NP


class SQLModelTtalNpRepository(ITtalNpRepository):

    def __init__(self, session: Session = get_session()):
        self.session = session

    def create_ttal_np(self, project_id: str, codigo: str, asunto: str, ttal_np_file: str):
        ttal_np_db = Transmittal_NP(
            project_id=project_id,
            codigo=codigo,
            asunto=asunto,
            ttal_np_file=ttal_np_file
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
