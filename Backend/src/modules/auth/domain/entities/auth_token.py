from pydantic import BaseModel
from uuid import UUID
class AuthUser(BaseModel):
    id: UUID
    name: str
    email: str
    role: str


    
class AuthToken(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    user: AuthUser