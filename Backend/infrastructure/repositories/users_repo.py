from sqlmodel import Session
from core.interfaces.users import IUserRepository
from models.users import User
from typing import List, Optional
from sqlmodel import select

class SQLModelUserRepository(IUserRepository):
    def __init__(self, session: Session):
        self.session = session

    async def create_user(self, email: str, password: str, is_active: bool = False, is_epen_user: bool = False, is_admin: bool = False) -> User:
        user = User(email=email, password=password, is_active=is_active, is_epen_user=is_epen_user, is_admin=is_admin)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_user_by_email(self, email: str) -> Optional[User]:
        return await self.session.exec(select(User).where(User.email == email)).first()

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        return await self.session.get(User, user_id)

    async def list_users(self) -> List[User]:
        return await self.session.exec(select(User)).all()