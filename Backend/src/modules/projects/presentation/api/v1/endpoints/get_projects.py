from fastapi import APIRouter, Depends, HTTPException, status, Header, Response
from typing import Optional, List
from src.modules.projects.presentation.api.v1.dependencies import get_project_uc
from src.modules.projects.application.use_cases import ProjectUseCase
# from src.modules.projects.application.dtos import ProjectDTO
from src.domain.entities.projects import Project
from src.domain.entities.users import User
from src.infrastucture.database.database import get_session
import jwt
import os
from sqlmodel import Session


get_projects_router = APIRouter(prefix="/projects")

async def get_current_user(db: Session = Depends(get_session), authorization: Optional[str] = Header(None)) -> User:
    if not authorization:
        print("Authorization header missing")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization header missing")
    token = authorization.split(" ")[1] if " " in authorization else None

    if not token:
        print("Invalid authorization header format:", authorization)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authorization header format")
    
    payload = jwt.decode(token, os.getenv("JWT_SECRET_KEY"), algorithms=[os.getenv("JWT_ALGORITHM")])
    user_id = payload.get("sub")

    if not user_id:
        print("Invalid token payload:", payload)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
    user_athenticated:User = db.get(User, user_id)

    if not user_athenticated:
        print ("User not found for ID:", user_id)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user_athenticated
    

@get_projects_router.get("/", response_model=List[Project], status_code=status.HTTP_200_OK)
async def get_projects(project_uc: ProjectUseCase = Depends(get_project_uc), user: User = Depends(get_current_user)):
    return Response(content="This endpoint is under construction", status_code=status.HTTP_200_OK)
    # try:
    #     projects: List[Project] = await project_uc.list_projects(user.id)
    #     return [project for project in projects]
    # except Exception as e:
    #     raise HTTPException(status_code=400, detail=str(e))