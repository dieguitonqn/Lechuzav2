from domain.interfaces.file_management import IFileManager
from fastapi import UploadFile
from pathlib import Path
import os


class FileManager(IFileManager):
    async def save_file(self, file: UploadFile, destination_path: str) -> str:
        try:
            # file.filename puede ser None, usamos un valor por defecto
            filename = Path(
                file.filename or "unnamed_file"
            ).name  # evita subdirectorios maliciosos en el nombre
            
            # Convertir destination_path a Path para poder usar el operador /
            dest_path = Path(destination_path)
            
            if not dest_path.exists():
                dest_path.mkdir(parents=True, exist_ok=True)
            
            full_path = dest_path / filename
            with open(full_path, "wb") as f:
                f.write(file.file.read())
            
            return str(full_path)
        except Exception as e:
            print(f"Error saving file: {e}")
            return ""

    async def delete_file(self, file_path: str) -> bool:
        try:
            os.remove(file_path)
            return True
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False

    async def save_document(self, file_data: bytes, destination_path: str) -> str:
        try:
            with open(destination_path, "wb") as f:
                f.write(file_data)
            return str(destination_path)
        except Exception as e:
            print(f"Error saving document file: {e}")
            return ""

    async def delete_document(self, file_path: str) -> bool:
        try:
            os.remove(file_path)
            return True
        except Exception as e:
            print(f"Error deleting document file: {e}")
            return False
