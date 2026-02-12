from fastapi import UploadFile
import uuid


class ProjectCreateDTO:
    def __init__(
        self,
        name: str,
        code: str,
        description: str,
        project_file: UploadFile,
        company_id: uuid.UUID,
    ):
        self.name = name
        self.description = description
        self.code = code
        self.project_file = project_file
        self.company_id = company_id
class ProjectDTO:
    def __init__(
        self,
        id: str,
        name: str,
        code: str,
        description: str,
        project_file: str,
        company_id: str,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.code = code
        self.project_file = project_file
        self.company_id = company_id