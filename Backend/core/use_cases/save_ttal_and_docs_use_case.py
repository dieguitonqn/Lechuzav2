from pathlib import Path
from core.dtos.ttal_np_documents import TtalNpDTO
from models.ttals_nps import Transmittal_NP
from infrastructure.repositories.ttal_np_repo import ITtalNpRepository
from infrastructure.repositories.document_repo import IDocumentRepository
from infrastructure.storage.file_managment_repo import IFileManager

class SaveTtalAndDocsUseCase:
    def __init__(self, ttal_repo: ITtalNpRepository, document_repo: IDocumentRepository, file_manager: IFileManager):
        self.ttal_repo = ttal_repo
        self.document_repo = document_repo
        self.file_manager = file_manager

    def execute(self, ttal_dto: TtalNpDTO):

        # Save ttal file first, return ttal path
        
        file_dir = Path("files") / ttal_dto.project_id

        ttal_np_path = self.file_manager.save_ttal(file_data=ttal_dto.ttal_np_file, destination_path=file_dir)
        if not ttal_np_path:
            raise Exception("Failed to save TTAL-NP file")

        # create the ttal record in DB
        ttal_np: Transmittal_NP = self.ttal_repo.create_ttal_np(
            project_id=ttal_dto.project_id,
            codigo=ttal_dto.ttal_np_code,
            asunto=ttal_dto.ttal_np_description,
            ttal_np_file=ttal_np_path
        )
        if not ttal_np:
            raise Exception("Failed to create TTAL-NP record")
        
        # Now save each document and link to the ttal
        for doc_dto in ttal_dto.documents:
            # Save document file, return document path
            document_path = self.file_manager.save_document(doc_dto.document_file)
            if not document_path:
                raise Exception(f"Failed to save document file: {doc_dto.name}")

            # create the document record in DB, linking to the ttal_np
            document = self.document_repo.create_document(
                codigo=doc_dto.code,
                nombre=doc_dto.name,
                revision=doc_dto.revision,
                document_file=document_path,
                project_id=doc_dto.project_id,
                ttal_np_id=ttal_np.id
            )
            if not document:
                raise Exception(f"Failed to create document record: {doc_dto.name}")