from fastapi import APIRouter, Depends, HTTPException, status, Form, UploadFile, File
from typing import List
from core.use_cases.ttal_and_docs_uc import SaveTtalAndDocsUseCase
from core.dtos.ttal_np_documents import TtalNpDTO, DocumentDataDTO
from api.v1.dependencies.get_save_ttal_docs_uc import get_save_ttal_and_docs_uc

ttal_documents = APIRouter( prefix="/ttal-docs")

@ttal_documents.post("/", status_code=status.HTTP_200_OK)
async def upload_ttal_document(
    project_id: str = Form(...),
    
    ttal_np_code: str = Form(...),
    ttal_np_file: UploadFile = File(...),
    ttal_np_description: str = Form(...),

    document_code: List[str] = Form(...),
    document_name: List[str] = Form(...),
    document_revision: List[str] = Form(...),
    document_file: List[UploadFile] = File(...),
        #Inyecto la dependencia del caso de uso instanciando la clase
    # save_ttal_and_docs_
    use_case: SaveTtalAndDocsUseCase = Depends(get_save_ttal_and_docs_uc)
    
    ):

    
   
    if len(document_code) != len(document_name) or len(document_code) != len(document_revision) or len(document_code) != len(document_file):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mismatched document fields")

    if not project_id or not ttal_np_code or not ttal_np_file or not ttal_np_description:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing transmittal fields")

    document_list = []
    for code, name, revision, doc_file in zip(document_code, document_name, document_revision, document_file):
        document = DocumentDataDTO(
            code=code,
            name=name,
            revision=revision,
            document_file=doc_file,
            project_id=project_id
        )
        document_list.append(document)
    ttal_np_dto = TtalNpDTO(
        project_id=project_id,
        ttal_np_code=ttal_np_code,
        ttal_np_file=ttal_np_file,
        ttal_np_description=ttal_np_description,
        documents=document_list
    )


   
   #paso el DTO al servicio para que lo procese
    
    try:
        await use_case.execute(ttal_np_dto)
        return {"message": "Transmittal and documents uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


   
   