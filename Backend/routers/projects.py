from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response, status, Cookie, Request
from models import Project, User
from database import get_session, Session
from auth import SECRET_KEY, ALGORITHM, create_access_token
import jwt
from sqlmodel import Session,select, filter, first

router = APIRouter()

@router.post("/project", status_code=status.HTTP_201_CREATED)
async def create_project(project: Project, session: Session = Depends(get_session), access_token: Annotated[str, Cookie()]=None):
    if not access_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])

    email = payload.get("sub")
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    if session.exec(select(User).where(User.email == email)).first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    session.add(project)
    session.commit()
    session.refresh(project)
    return project