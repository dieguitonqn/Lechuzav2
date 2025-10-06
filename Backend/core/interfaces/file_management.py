from abc import ABC, abstractmethod
from typing import List

class IFileManager(ABC):

    @abstractmethod
    async def save_ttal(self, file_data: bytes, destination_path: str) -> str:
        pass

    @abstractmethod
    async def delete_ttal(self, file_path: str) -> bool:
        pass

    @abstractmethod
    async def save_document(self, file_data: bytes, destination_path: str) -> str:
        pass

    @abstractmethod
    async def delete_document(self, file_path: str) -> bool:
        pass