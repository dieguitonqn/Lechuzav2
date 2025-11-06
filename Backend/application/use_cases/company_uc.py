from domain.interfaces.company_interface import ICompany
from domain.entities.companies import Company
from application.dtos.company_dto import CompanyDTO


class CompanyUseCase:
    def __init__(self, company_repository: ICompany):
        self.company_repository = company_repository

    def create_company(self, company_dto: CompanyDTO) -> Company:
        # Logic to create a company
        try:
            new_company: Company = self.company_repository.create_company(
                name=company_dto.nombre, codigo=company_dto.codigo
            )
            return new_company
        except Exception as e:
            raise e
