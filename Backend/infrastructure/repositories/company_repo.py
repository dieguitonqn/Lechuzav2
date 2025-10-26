from domain.interfaces.company_interface import ICompany
from sqlmodel import Session
from infrastructure.database.database import get_session


class SQLModelCompanyRepository(ICompany):
    def __init__(self, session: Session = get_session):
        self.session = session

    def create_company(self, name: str, codigo: str):
        from domain.entities.companies import (
            Company,
        )  # Importar aquí para evitar dependencias circulares

        company_db = Company(nombre=name, codigo=codigo)
        try:
            self.session.add(company_db)
            self.session.commit()
            self.session.refresh(company_db)
            return company_db
        except Exception as e:
            print(f"Error creating Company: {e}")
            self.session.rollback()
            return None
