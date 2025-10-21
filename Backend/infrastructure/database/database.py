
from sqlmodel import create_engine, Session, SQLModel
from infrastructure.database.config import settings

# Configura el engine de SQLModel(SQLAlchemy) para PostgreSQL


engine = create_engine(settings.database_url, echo=True, pool_recycle=3600) # echo=True para ver las queries SQL en consola

def create_db_and_tables():
    """
    Crea las tablas en la base de datos importando todos los modelos.
    Los imports están dentro de la función para evitar imports circulares.
    """
    # Importar las clases de modelo para que SQLModel las registre
    from domain.entities.users import User
    from domain.entities.projects import Project
    from domain.entities.companies import Company
    from domain.entities.documents import Document
    from domain.entities.statuses import Status
    from domain.entities.correction_reports import CorrectionReport
    from domain.entities.models_links import ProjectUserLink
    from domain.entities.ttals_nps import Transmittal_NP
    
    # Crear las tablas basándose en los modelos importados
    SQLModel.metadata.create_all(engine)

    # Para producción se utiliza Alembic para manejar las migraciones de la base de datos

def get_session():
    """
    Función de dependencia para FastAPI que proporciona una sesión de base de datos.
    Asegura que la sesión se cierre después de cada solicitud.
    """
    with Session(engine) as session:
        yield session               # Devuelve la sesión para que se use en las rutas de FastAPI. El yield es para que la sesión se cierre automáticamente al finalizar la solicitud.
        session.close()             # Cierra la sesión al finalizar la solicitud