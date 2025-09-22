from typing import Generator
from sqlmodel import create_engine, Session
from config import settings

# Configura el engine de SQLModel(SQLAlchemy) para PostgreSQL


engine = create_engine(settings.database_url, echo=True, pool_recycle=3600) # echo=True para ver las queries SQL en consola

def create_db_and_tables():
    # Se crean las tablas en la base de datos en modo development
    from models.users import SQLModel             # Importa los modelos del archivo models.py para que SQLModel los use para hacer las tablas
    from models.projects import SQLModel
    from models.companies import SQLModel
    from models.documents import SQLModel
    from models.statuses import SQLModel
    from models.correction_reports import SQLModel
    from models.models_links import SQLModel
    SQLModel.metadata.create_all(engine)    # Crea las tablas en la base de datos si no existen. Si existen, no hace nada.

    # Para producción se utiliza Alembic para manejar las migraciones de la base de datos

def get_session():
    """
    Función de dependencia para FastAPI que proporciona una sesión de base de datos.
    Asegura que la sesión se cierre después de cada solicitud.
    """
    with Session(engine) as session:
        yield session               # Devuelve la sesión para que se use en las rutas de FastAPI. El yield es para que la sesión se cierre automáticamente al finalizar la solicitud.
        session.close()             # Cierra la sesión al finalizar la solicitud