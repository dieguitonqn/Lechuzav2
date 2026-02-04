from fastapi import APIRouter, Depends
from sqlmodel import Session


from presentation.api.v1.dependencies.get_auth_uc import get_auth_uc
from infrastructure.database.database import get_session