from domain.interfaces.file_management import IFileManager
from fastapi import UploadFile
from pathlib import Path
import os


class FileManager(IFileManager):

    async def save_file(self, file: UploadFile, destination_path: str) -> str:
        try:
            filename = Path(file.filename).name  # evita subdirectorios maliciosos en el nombre
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            with open(destination_path / filename, "wb") as f:
                f.write(file.file.read())
            path: Path = destination_path / filename
            return str(path)
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
