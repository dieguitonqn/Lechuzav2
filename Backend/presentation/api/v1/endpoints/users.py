
from fastapi import APIRouter, Depends, HTTPException, status, Form
from application.dtos.users_create import UserCreateDTO
from presentation.api.v1.dependencies.get_user_create import get_user_create_use_case
from application.use_cases.users_uc import CreateUserUseCase


users = APIRouter(prefix="/users")


@users.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
        email: str = Form(...),
        password: str = Form(...),
        users_use_case: CreateUserUseCase = Depends(get_user_create_use_case)):
    user_dto = UserCreateDTO(email=email, password=password,
                             is_active=False, is_epen_user=False, is_admin=False)

    try:
        users_use_case.execute(user_dto)
        return {"message": "User created successfully"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    # Logic to create a user
