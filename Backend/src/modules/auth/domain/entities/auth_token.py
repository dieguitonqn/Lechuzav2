from pydantic import BaseModel

class AuthUser(BaseModel):
    id: int
    name: str
    email: str
    role: str


    
class AuthToken(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    user: AuthUser