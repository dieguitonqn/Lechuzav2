
from src.domain.entities.ttals_nps import Transmittal_NP
from src.domain.entities.users import User
from src.modules.documents.application.dtos import TtalNPDTO
from src.modules.documents.domain.interfaces import ITransmittalNPRepository
from sqlmodel import Session, select

import os
from pathlib import Path

class Ttal_nps_Repository(ITransmittalNPRepository):
    def __init__(self, session: Session):
        # Inicializar con la sesión recibida como parámetro
        self.session = session
    
    async def save_transmittal_np_file(self, ttal_dto:TtalNPDTO, user:User, dirpath: Path) -> str:
        # Aquí iría la lógica para guardar el archivo del TTAL_NP en el sistema de archivos o servicio de almacenamiento
        
        sanitized_filename = f"TtalNP-{ttal_dto.obra_slug}_{ttal_dto.np_ttal}_{ttal_dto.np_ttal_descripcion}.pdf"
        sanitized_filename = sanitized_filename.replace(" ", "_")
       
        try:
            os.makedirs(dirpath, exist_ok=True)
        except OSError as e:
            raise RuntimeError(f"Error creating directory {dirpath}: {e}")
        

        file_path = os.path.join(dirpath, sanitized_filename)
        try:
            with open(file_path, "wb") as f:
                content = await ttal_dto.np_ttal_file.read()
                f.write(content)
        except OSError as e:
            raise RuntimeError(f"Error writing file {file_path}: {e}")
        return file_path
        
        
    async def save_transmittal_np_toDB(self, ttal_np:Transmittal_NP, user:User):
        # Aquí iría la lógica para guardar el TTAL_NP en la base de datos
        # Podrías usar un ORM como SQLAlchemy o SQLModel para interactuar con la base
        existing_ttals_np = self.session.exec(
            select(Transmittal_NP).where(
                Transmittal_NP.codigo == ttal_np.codigo,
                Transmittal_NP.project_id == ttal_np.project_id
            )
        ).first()
        
        if existing_ttals_np:
            raise ValueError("El TTAL_NP ya existe en la base de datos")
        
        try:
            self.session.add(ttal_np)
            self.session.commit()
            self.session.refresh(ttal_np)
            return ttal_np.id
        except Exception as e:
            self.session.rollback()
            raise RuntimeError(f"Error saving TTAL_NP to the database: {e}")