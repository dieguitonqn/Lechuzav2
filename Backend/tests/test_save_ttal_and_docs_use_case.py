import pytest
from unittest.mock import MagicMock, patch
from Backend.core.use_cases.ttal_and_docs_uc import SaveTtalAndDocsUseCase
from core.dtos.ttal_np_documents import TtalNpDTO, DocumentDataDTO
from models.ttals_nps import Transmittal_NP
from infrastructure.repositories.document_repo import SQLModelDocumentRepository
from models.documents import Document

class DummyFileManager:
    def save_ttal(self, file_data, destination_path):
        return f"{destination_path}/ttal_np.pdf"
    def save_document(self, file_data):
        return f"files/{file_data}.pdf"

class DummyTtalNpRepo:
    def create_ttal_np(self, project_id, codigo, asunto, ttal_np_file):
        return Transmittal_NP(id=1, project_id=project_id, codigo=codigo, asunto=asunto, ttal_np_file=ttal_np_file)

class DummyDocumentRepo:
    def create_document(self, codigo, nombre, revision, document_file, project_id, ttal_np_id):
        return MagicMock(id=1, codigo=codigo, nombre=nombre, revision=revision, document_file=document_file, project_id=project_id, ttal_np_id=ttal_np_id)

@pytest.fixture
def use_case():
    return SaveTtalAndDocsUseCase(
        ttal_repo=DummyTtalNpRepo(),
        document_repo=DummyDocumentRepo(),
        file_manager=DummyFileManager()
    )

def test_execute_success(use_case):
    mock_document_repo = patch('infrastructure.repositories.document_repo.SQLModelDocumentRepository', autospec=True)
    mock_document_repo.return_value.create_document = Document(id=1, codigo="DOC-001", nombre="Documento 1", revision="A", document_file="doc_file_1", project_id="1234", ttal_np_id=1)
    ttal_dto = TtalNpDTO(
        project_id="1234",
        ttal_np_file="ttal_file",
        ttal_np_code="NP-001",
        ttal_np_description="Test TTAL-NP",
        documents=[
            DocumentDataDTO(
                code="DOC-001",
                name="Documento 1",
                revision="A",
                document_file="doc_file_1",
                project_id="1234"
            ),
            DocumentDataDTO(
                code="DOC-002",
                name="Documento 2",
                revision="B",
                document_file="doc_file_2",
                project_id="1234"
            )
        ]
    )
    use_case.execute(ttal_dto)


# def test_execute_fail_save_ttal(use_case):
#     use_case.file_manager.save_ttal = MagicMock(return_value=None)
#     ttal_dto = TtalNpDTO(
#         project_id="1234",
#         ttal_np_file="ttal_file",
#         ttal_np_code="NP-001",
#         ttal_np_description="Test TTAL-NP",
#         documents=[]
#     )
#     with pytest.raises(Exception, match="Failed to save TTAL-NP file"):
#         use_case.execute(ttal_dto)


# def test_execute_fail_create_ttal(use_case):
#     use_case.file_manager.save_ttal = MagicMock(return_value="/files/ttal_np.pdf")
#     use_case.ttal_repo.create_ttal_np = MagicMock(return_value=None)
#     ttal_dto = TtalNpDTO(
#         project_id="1234",
#         ttal_np_file="ttal_file",
#         ttal_np_code="NP-001",
#         ttal_np_description="Test TTAL-NP",
#         documents=[]
#     )
#     with pytest.raises(Exception, match="Failed to create TTAL-NP record"):
#         use_case.execute(ttal_dto)


# def test_execute_fail_save_document(use_case):
#     use_case.file_manager.save_ttal = MagicMock(return_value="/files/ttal_np.pdf")
#     use_case.ttal_repo.create_ttal_np = MagicMock(return_value=Transmittal_NP(id=1, project_id="1234", codigo="NP-001", asunto="Test TTAL-NP", ttal_np_file="/files/ttal_np.pdf"))
#     use_case.file_manager.save_document = MagicMock(return_value=None)
#     ttal_dto = TtalNpDTO(
#         project_id="1234",
#         ttal_np_file="ttal_file",
#         ttal_np_code="NP-001",
#         ttal_np_description="Test TTAL-NP",
#         documents=[
#             DocumentDataDTO(
#                 code="DOC-001",
#                 name="Documento 1",
#                 revision="A",
#                 document_file="doc_file_1",
#                 project_id="1234"
#             )
#         ]
#     )
#     with pytest.raises(Exception, match="Failed to save document file: Documento 1"):
#         use_case.execute(ttal_dto)


# def test_execute_fail_create_document(use_case):
#     use_case.file_manager.save_ttal = MagicMock(return_value="/files/ttal_np.pdf")
#     use_case.ttal_repo.create_ttal_np = MagicMock(return_value=Transmittal_NP(id=1, project_id="1234", codigo="NP-001", asunto="Test TTAL-NP", ttal_np_file="/files/ttal_np.pdf"))
#     use_case.file_manager.save_document = MagicMock(return_value="files/doc_file_1.pdf")
#     use_case.document_repo.create_document = MagicMock(return_value=None)
#     ttal_dto = TtalNpDTO(
#         project_id="1234",
#         ttal_np_file="ttal_file",
#         ttal_np_code="NP-001",
#         ttal_np_description="Test TTAL-NP",
#         documents=[
#             DocumentDataDTO(
#                 code="DOC-001",
#                 name="Documento 1",
#                 revision="A",
#                 document_file="doc_file_1",
#                 project_id="1234"
#             )
#         ]
#     )
#     with pytest.raises(Exception, match="Failed to create document record: Documento 1"):
#         use_case.execute(ttal_dto)
