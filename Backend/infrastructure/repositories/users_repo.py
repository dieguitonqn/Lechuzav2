from sqlmodel import Session
from domain.interfaces.users import IUserRepository
from domain.entities.users import User
from typing import List, Optional
from sqlmodel import select

class SQLModelUserRepository(IUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, email: str, password: str, is_active: bool = False, is_epen_user: bool = False, is_admin: bool = False) -> User:
        user = User(email=email, 
                    password=password, 
                    is_active=is_active, 
                    is_epen_user=is_epen_user, 
                    is_admin=is_admin)
        
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        return  self.session.exec(select(User).where(User.email == email)).first()

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        return  self.session.get(User, user_id)

    def list_users(self) -> List[User]:
        return  self.session.exec(select(User)).all()