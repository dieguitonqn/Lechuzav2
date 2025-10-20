from abc import ABC, abstractmethod
from typing import List


class IDocumentRepository(ABC):

    @abstractmethod
    async def create_document(self, codigo: str, 
                              nombre: str, 
                              revision: str, 
                              document_file: str, 
                              project_id: str,
                              ttal_np_id: str = None):
        pass

