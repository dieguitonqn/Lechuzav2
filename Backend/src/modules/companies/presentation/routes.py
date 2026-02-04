from fastapi import APIRouter, Depends, HTTPException, status

# For now, reuse existing use case and DTOs from current layers.
from presentation.api.v1.dependencies.get_company_uc import get_company_uc
from application.use_cases.company_uc import CompanyUseCase
from application.dtos.company_dto import CompanyDTO
from domain.entities.companies import CompanyEndpoint, Company

router = APIRouter(prefix="/companies")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_company(
    company: CompanyEndpoint, company_uc: CompanyUseCase = Depends(get_company_uc)
):
    company_dto = CompanyDTO(
        nombre=company.name,
        codigo=company.code,
    )
    try:
        company_db: Company = company_uc.create_company(company_dto)
        return {
            "message": "Company created successfully",
            "name": company_db.nombre,
            "codigo": company_db.codigo,
            "id": company_db.id,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
