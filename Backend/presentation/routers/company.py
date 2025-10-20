# from fastapi import APIRouter, Depends, HTTPException, status, Cookie
# from typing import Annotated
# from sqlmodel import Session, select
# import jwt
# from infrastructure.database.database import get_session
# from domain.entities.companies import Company
# from domain.entities.users import User


# router = APIRouter()

# @router.post("/company", status_code=status.HTTP_201_CREATED)
# async def create_company(company: Company, session: Session = Depends(get_session)):
    
#     company_in_db = session.exec(select(Company).where(Company.nombre == company.nombre)).first()
#     if company_in_db:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Company already exists")
    
#     new_company = Company(nombre=company.nombre, codigo=company.codigo)
#     session.add(new_company)
#     session.commit()
#     session.refresh(new_company)
#     return new_company

