from core.interfaces.users import IUserRepository
from core.dtos.users_dto import UserCreateDTO



class CreateUserUseCase:
    def __init__(self, user_repo:IUserRepository):
        self.user_repository = user_repo

    def execute(self, user_create_dto:UserCreateDTO):
        # Validate input data
        if not user_create_dto.email or not user_create_dto.password:
            raise ValueError("Email and password are required")

        # Check if user already exists
        existing_user = self.user_repository.get_user_by_email(user_create_dto.email)
        if existing_user:
            raise ValueError("User with this email already exists")

        # Save the new user to the repository
        created_user = self.user_repository.create_user(user_create_dto.email, user_create_dto.password)

        return created_user != None and created_user