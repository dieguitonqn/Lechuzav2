from abc import ABC, abstractmethod
from fastapi import UploadFile

class IFileManager(ABC):

    @abstractmethod
    async def save_file(self, file: UploadFile, destination_path: str) -> str:
        pass

    @abstractmethod
    async def delete_file(self, file_path: str) -> bool:
        pass

    @abstractmethod
    async def save_document(self, file_data: bytes, destination_path: str) -> str:
        pass

    @abstractmethod
    async def delete_document(self, file_path: str) -> bool:
        pass