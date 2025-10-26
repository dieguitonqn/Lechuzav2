from sqlmodel import create_engine, Session, SQLModel
from infrastructure.database.config import settings

# Configura el engine de SQLModel(SQLAlchemy) para PostgreSQL


engine = create_engine(
    settings.database_url, echo=True, pool_recycle=3600
)  # echo=True para ver las queries SQL en consola


def create_db_and_tables():
    """
    Crea las tablas en la base de datos importando todos los modelos.
    Los imports están dentro de la función para evitar imports circulares.
    """
    # Importar el paquete de entidades para registrar todos los modelos.
    # Usamos importlib para evitar "unused import" warnings de linters y
    # para no necesitar listar cada modelo individualmente.
    import importlib

    # Importa el paquete que a su vez importa/reexporta los modelos
    # (ver `domain/entities/__init__.py`) — esto provoca los side-effects necesarios
    # para que SQLModel registre las clases.
    importlib.import_module("domain.entities")

    # Crear las tablas basándose en los modelos importados
    SQLModel.metadata.create_all(engine)

    # Para producción se utiliza Alembic para manejar las migraciones de la base de datos


def get_session():
    """
    Función de dependencia para FastAPI que proporciona una sesión de base de datos.
    Asegura que la sesión se cierre después de cada solicitud.
    """
    with Session(engine) as session:
        yield session  # Devuelve la sesión para que se use en las rutas de FastAPI. El yield es para que la sesión se cierre automáticamente al finalizar la solicitud.
        session.close()  # Cierra la sesión al finalizar la solicitud
