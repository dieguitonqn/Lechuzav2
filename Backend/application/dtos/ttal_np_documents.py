from fastapi import UploadFile
import uuid


# DTO para documentos del TTAL-NP
class DocumentDataDTO:
    def __init__(
        self,
        code: str,
        name: str,
        revision: str,
        document_file: UploadFile,
        project_id: uuid.UUID,
    ):
        self.code = code
        self.name = name
        self.revision = revision
        self.document_file = document_file
        self.project_id = project_id


class TtalNpDTO:
    def __init__(
        self,
        project_id: uuid.UUID,
        ttal_np_code: str,
        ttal_np_file: UploadFile,
        ttal_np_description: str,
        documents: list[DocumentDataDTO],
    ):
        self.project_id = project_id
        self.ttal_np_code = ttal_np_code
        self.ttal_np_file = ttal_np_file
        self.ttal_np_description = ttal_np_description
        self.documents = documents
