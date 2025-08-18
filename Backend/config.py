from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env", #lugar en donde se encuentra el archivo .env
        extra="ignore"      # Ignorar variables no definidas en el modelo Settings. En este caso, solo "cargar" la variable database_url
        )

@lru_cache()                #cachea el resultado para evitar lecturas repetidas del archivo .env
def get_settings():
    return Settings()       #Devuelve una instancia de Settings con los valores cargados desde el archivo .env

settings = get_settings()   # Instancia de configuración que se puede usar en otras partes del código
# settings.database_url es la URL de conexión a la base de datos, por ejemplo: "postgresql://user:password@localhost/dbname"
# Se puede acceder a otras variables definidas en el archivo .env de la misma manera. Agregás a Settings las variables que necesites.