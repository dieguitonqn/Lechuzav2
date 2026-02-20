from fastapi import APIRouter, Depends, Request
from sqlmodel import Session


from presentation.api.v1.dependencies.get_auth_uc import get_auth_uc
from src.infrastucture.database.database import get_session


refresh_router = APIRouter()

@refresh_router.post("/refresh")
async def refresh_token(
    request:Request,
    db: Session = Depends(get_session),
    auth_uc = Depends(get_auth_uc),
    refresh_token: str = None
):
    """
    Endpoint to refresh access token using a valid refresh token.
    """
    # Implementation would go here, e.g.:
    # 1. Extract refresh token from request (e.g. from cookies or body)
    # body = await request.json()
    # refresh_token = body.get("refresh_token")
    # 2. Validate refresh token and generate new access token
    
    # 3. Return new access token (and possibly a new refresh token)
    return {"message": "Token refreshed successfully"}