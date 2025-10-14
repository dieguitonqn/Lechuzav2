from fastapi import Depends, APIRouter, HTTPException, UploadFile, status
from sqlmodel import Session
from typing import List
from api.v1.dependencies.get_company_uc import get_company_uc
from core.use_cases.company_uc import CompanyUseCase
from models.companies import CompanyEndpoint, Company

companies=APIRouter(prefix="/companies")

@companies.post("/", status_code=status.HTTP_201_CREATED)
async def create_company(company: CompanyEndpoint,
                         company_uc: CompanyUseCase = Depends(get_company_uc)):
    try:
        company:Company = await company_uc.create_company(company.name, company.code)
        return {"message": "Company created successfully", "name": company.nombre, "codigo": company.codigo, "id": company.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
