from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select
from schemas import UserCreate
from models import User
from database import get_session

users = APIRouter()




@users.post("/user/create", response_model=UserCreate, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: Session = Depends(get_session)):
    print(user)
    db_user = User(
        email=user.email,
        google_id=user.google_id,
        password=user.password,
    )
    print(db_user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return user











# @users.get("/users", response_model=List[User])
# def read_users(session: Session = Depends(get_session)):
#     statement = select(User)
#     results = session.exec(statement)
#     return results.all()

# @users.get("/user/{user_id}", response_model=User)
# def read_user(user_id: int, session: Session = Depends(get_session)):
#     user = session.get(User, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# @users.put("/user/{user_id}", response_model=User)
# def update_user(user_id: int, user: User, session: Session = Depends(get_session)):
#     db_user = session.get(User, user_id)
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     for key, value in user.dict(exclude_unset=True).items():
#         setattr(db_user, key, value)
    
#     session.add(db_user)
#     session.commit()
#     session.refresh(db_user)
#     return db_user