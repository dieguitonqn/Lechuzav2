import datetime
from sqlmodel import Field,  SQLModel



class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str | None = None
    email: str = Field(index=True, unique=True)
    google_id: str | None = Field(index=True, unique=True) 
    password: str | None = None
    is_active: bool = True
    is_verified: bool = False
    is_admin: bool = False
    birth_date: datetime.datetime | None = None
    profile_picture_url: str | None = None
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now, sa_column_kwargs={"onupdate": datetime.datetime.now})


# class Project(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     name: str
#     description: str | None = None
#     user_id: int = Field(foreign_key="user.id")
#     created_at: datetime.datetime = Field(default=datetime.datetime.now)
#     updated_at: datetime.datetime = Field(default=datetime.datetime.now, sa_column_kwargs={"onupdate": datetime.datetime.now})
    
    

# class Task(SQLModel, table=True):
#     id:int = Field(default=None, primary_key=True)
#     name:str
#     description:str | None = None
#     project_id:int = Field(foreign_key="projects.id")
#     user_id:int = Field(foreign_key="user.id")
#     status:str = Field(default="pending")       # pending, in_progress, completed
#     priority:str = Field(default="medium")      # low, medium, high
#     due_date:datetime.datetime | None = None
#     created_at:datetime.datetime = Field(default=datetime.datetime.now)
#     updated_at:datetime.datetime = Field(default=datetime.datetime.now, sa_column_kwargs={"onupdate": datetime.datetime.now})



# class Comments (SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     content: str
#     task_id: int = Field(foreign_key="task.id")
#     user_id: int = Field(foreign_key="user.id")
#     created_at: datetime.datetime = Field(default=datetime.datetime.now)
#     updated_at: datetime.datetime = Field(default=datetime.datetime.now, sa_column_kwargs={"onupdate": datetime.datetime.now})

