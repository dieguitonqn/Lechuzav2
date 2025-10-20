from fastapi import UploadFile
import uuid


class ProjectCreateDTO:
    def __init__(self, name: str, code:str, description: str, project_file:UploadFile, company_id:uuid.UUID):
        self.name = name
        self.description = description
        self.code = code
        self.project_file = project_file
        self.company_id = company_id
