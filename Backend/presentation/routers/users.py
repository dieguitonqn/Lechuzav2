# from typing import List
# import uuid
# from presentation.routers.auth import crypt
# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlmodel import Session, select

# from domain.entities.users import User,UserCreate
# from infrastructure.database.database import get_session

# users = APIRouter()




# @users.post("/prev_users", status_code=status.HTTP_201_CREATED)
# async def create_user(user: UserCreate, session: Session = Depends(get_session)):
#     db_user = User(
#         email=user.email,
#         password_hash=crypt.hash(user.password),
#         is_active=user.is_active,
#         is_epen_user=user.is_epen_user,
#         is_admin=user.is_admin
#     )
#     session.add(db_user)
#     session.commit()
#     session.refresh(db_user)
#     return True





# @users.get("/users", response_model=List[User], status_code=status.HTTP_200_OK)
# def read_users(session: Session = Depends(get_session)):
#     statement = select(User)
#     try:
#         results = session.exec(statement)
#         users_list = results.all()
#         return users_list
#     except Exception as e:
#         print("Error occurred:", e)
#         raise e  # Re-raise the exception after logging it
    

# @users.get("/users/{user_id}")
# def read_user(user_id: uuid.UUID, session: Session = Depends(get_session)):
#     db_user = session.get(User, user_id)
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")
#     print(f"Company Name: {db_user.company.nombre}")
#     print (f"Projects: {db_user.projects}")
#     return True