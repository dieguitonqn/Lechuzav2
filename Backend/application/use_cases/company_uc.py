from domain.interfaces.company_interface import ICompany
from domain.entities.companies import Company

class CompanyUseCase:
    def __init__(self, company_repository: ICompany):
        self.company_repository = company_repository

    def create_company(self, name: str, codigo: str):
        # Logic to create a company
        new_company:Company = self.company_repository.create_company(name=name, codigo=codigo)
        return new_company