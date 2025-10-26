from abc import ABC, abstractmethod


class ICompany(ABC):
    @abstractmethod
    def create_company(self, name: str, codigo: str):
        pass
