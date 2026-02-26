from abc import ABC


class IDocumentsRepository(ABC):
    
    def save_document_toDB(self, document, user):
        pass

class IDocsFilesRepository(ABC):
    
    async def save_file(self, file, filename):
        pass

    async def get_file(self, filename):
        pass

    async def delete_file(self, filename):
        pass

    async def update_file(self, filename, new_file):
        pass

class ITransmittalNPRepository(ABC):
    
    async def save_transmittal_np_file(self, ttal_dto, user)->str:
        pass

    async def save_transmittal_np_toDB(self, ttal_np, user):
        pass