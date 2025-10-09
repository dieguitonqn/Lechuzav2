from interfaces.company_interface import ICompany

class CompanyUseCase:
    def __init__(self, company_repository: ICompany):
        self.company_repository = company_repository

    async def create_company(self, name: str, codigo: str):
        # Logic to create a company
        new_company = await self.company_repository.create(name=name, codigo=codigo)
        return new_company