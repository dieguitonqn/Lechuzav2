from fastapi import Depends, APIRouter, HTTPException, UploadFile, status
from presentation.api.v1.dependencies.get_company_uc import get_company_uc
from application.use_cases.company_uc import CompanyUseCase
from domain.entities.companies import CompanyEndpoint, Company

companies=APIRouter(prefix="/companies")

@companies.post("/", status_code=status.HTTP_201_CREATED)
def create_company(company: CompanyEndpoint,
                         company_uc: CompanyUseCase = Depends(get_company_uc)):
    try:
        company:Company = company_uc.create_company(company.name, company.code)
        return {"message": "Company created successfully", "name": company.nombre, "codigo": company.codigo, "id": company.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
