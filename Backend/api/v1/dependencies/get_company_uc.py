
from core.use_cases.company_uc import CompanyUseCase
from database.database import get_session
from fastapi import Depends 
from sqlmodel import Session
from infrastructure.repositories.company_repo import SQLModelCompanyRepository


def get_company_uc(session: Session=Depends(get_session)):
    company_repository = SQLModelCompanyRepository(session)
    return CompanyUseCase(company_repository)