from fastapi import APIRouter, HTTPException, Depends

from src.modules.auth.application.dtos.auth_dto import LoginRequest, LoginResponse
from src.modules.auth.application.use_cases.auth_uc import AuthUseCase
from src.modules.auth.presentation.api.v1.dependencies.get_auth_uc import get_auth_uc

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
async def login(
    login_data: LoginRequest,
    auth_uc: AuthUseCase = Depends(get_auth_uc)
) -> LoginResponse:
    """
    Authenticate user and return access token
    
    This endpoint matches the structure expected by NextAuth:
    - Accepts email and password
    - Returns access_token, refresh_token, token_type, and user data
    """
    try:
        # Authenticate user
        result = await auth_uc.login(login_data.email, login_data.password)
        
        if not result:
            print("Authentication failed for email:", login_data.email)
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )
        
        return result
        
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )
