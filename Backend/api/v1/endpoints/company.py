from fastapi import Depends, APIRouter, HTTPException, UploadFile, status
from sqlmodel import Session
from typing import List


company=APIRouter("/company",tags=["Company"])

@company.post("/", status_code=status.HTTP_201_CREATED)
async def create_company(name: str,
                         codigo: str,
                         company_uc: SaveCompanyUseCase = Depends(get_company_use_case)):
    try:
        company = await company_uc.create_company(name, codigo)
        return company
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
