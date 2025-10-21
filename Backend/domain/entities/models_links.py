import uuid
from sqlmodel import Field, SQLModel


class ProjectUserLink(SQLModel, table=True):
    project_id: uuid.UUID = Field(
        foreign_key="project.id", primary_key=True
    )
    user_id: uuid.UUID = Field(
        foreign_key="user.id", primary_key=True
    )
    can_view_docs: bool = Field(default=False)
    can_upload_docs: bool = Field(default=False)
    can_correct_docs: bool = Field(default=False)

