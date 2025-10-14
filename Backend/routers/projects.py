# from typing import Annotated
# from fastapi import APIRouter, Depends, HTTPException, Response, status, Cookie, Request, UploadFile, File, Form
# from models.users import User
# from models.projects import ProjectCreate, Project
# from database.database import get_session, Session
# # from auth import SECRET_KEY, ALGORITHM, create_access_token
# import jwt
# from sqlmodel import Session, select

# projects = APIRouter()

# @projects.post("/projects", status_code=status.HTTP_201_CREATED)
# async def create_project(
#     name: str = Form(...),
#     code: str = Form(...),
#     description: str = Form(None),
#     emails_notification: list[str] = Form(...),
#     contract: str = Form(None),
#     contract_file: UploadFile = File(...),
#     session: Session = Depends(get_session)
# ):
#     # Guardar el archivo PDF en modo binario
#     file_location = f"files/{contract_file.filename}"
#     with open(file_location, "wb") as f:
#         f.write(await contract_file.read())

#     new_project = Project(
#         nombre=name,
#         codigo=code,
#         descripcion=description,
#         emails_notificacion=emails_notification,
#         contrato=contract,
#         contrato_url=file_location
#     )
#     session.add(new_project)
#     session.commit()
#     session.refresh(new_project)
#     return new_project

# @projects.get("/projects", status_code=status.HTTP_200_OK)
# def read_projects(session: Session = Depends(get_session)):
#     projects: list[Project] = session.exec(select(Project)).all()
#     return projects