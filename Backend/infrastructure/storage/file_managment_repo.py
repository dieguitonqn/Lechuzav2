from core.interfaces.file_management import IFileManager
from fastapi import UploadFile
from pathlib import Path
import os


class FileManager(IFileManager):

    async def save_ttal(self, ttal_np_file: UploadFile, destination_path: str) -> str:
        try:
            filename = Path(ttal_np_file.filename).name  # evita subdirectorios maliciosos en el nombre
            with open(destination_path / filename, "wb") as f:
                f.write(ttal_np_file.file.read())
            return destination_path / filename
        except Exception as e:
            print(f"Error saving TTAL-NP file: {e}")
            return ""

    async def delete_ttal(self, file_path: str) -> bool:
        try:
            os.remove(file_path)
            return True
        except Exception as e:
            print(f"Error deleting TTAL-NP file: {e}")
            return False

    async def save_document(self, file_data: bytes, destination_path: str) -> str:
        try:
            with open(destination_path, "wb") as f:
                f.write(file_data)
            return destination_path
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
