from fastapi import APIRouter, Depends, HTTPException, status, Form
from src.modules.users.application.dtos import UserCreateDTO
from src.modules.users.presentation.dependencies import get_user_create_use_case
from src.modules.users.application.use_cases import CreateUserUseCase


router = APIRouter(prefix="/users")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    email: str = Form(...),
    password: str = Form(...),
    users_use_case: CreateUserUseCase = Depends(get_user_create_use_case),
):
    user_dto = UserCreateDTO(
        email=email,
        password=password,
        is_active=False,
        is_epen_user=False,
        is_admin=False,
    )

    try:
        users_use_case.execute(user_dto)
        return {"message": "User created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
