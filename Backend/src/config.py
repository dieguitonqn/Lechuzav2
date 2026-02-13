import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde la ruta correcta
backend_root = Path(__file__).parent.parent
env_path = backend_root / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
    
    # JWT Configuration
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_TOKEN_EXPIRE_HOURS: int = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_HOURS", "24"))
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_DAYS", "7"))
    
    def __post_init__(self):
        """Validar configuraciones críticas"""
        if not self.JWT_SECRET_KEY:
            raise ValueError("JWT_SECRET_KEY no encontrada en las variables de entorno. Verifica tu archivo .env")
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL no encontrada en las variables de entorno. Verifica tu archivo .env")


# Instancia global de configuración
settings = Settings()