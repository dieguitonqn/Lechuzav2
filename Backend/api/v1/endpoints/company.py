from fastapi import Depends, APIRouter, HTTPException, UploadFile, status
from sqlmodel import Session
from typing import List
from api.v1.dependencies import get_session, get_company_uc
from core.use_cases.company_uc import CompanyUseCase

company=APIRouter("/company",tags=["Company"])

@company.post("/", status_code=status.HTTP_201_CREATED)
async def create_company(name: str,
                         codigo: str,
                         company_uc: CompanyUseCase = Depends(get_company_uc)):
    try:
        company = await company_uc.create_company(name, codigo)
        return company
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
