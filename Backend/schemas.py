from pydantic import BaseModel, Field
import datetime


class UserBase(BaseModel):
    id: int | None = None
    name: str | None = None
    email: str | None = None
    google_id: str | None = None
    is_active: bool = True
    is_verified: bool = False
    is_admin: bool = False
    birth_date: datetime.datetime | None = None
    profile_picture_url: str | None = None
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)



class User(UserBase):
    password: str | None = None
    

class UserCreate(BaseModel):
    email: str
    google_id: str | None = None
    password: str


