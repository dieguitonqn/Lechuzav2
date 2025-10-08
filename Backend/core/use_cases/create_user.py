from core.interfaces.users import IUserRepository



class CreateUserUseCase:
    def __init__(self, user_repository:IUserRepository):
        self.user_repository = user_repository

    def execute(self, user_create_dto):
        # Validate input data
        if not user_create_dto.email or not user_create_dto.password:
            raise ValueError("Email and password are required")

        # Check if user already exists
        existing_user = self.user_repository.get_by_email(user_create_dto.email)
        if existing_user:
            raise ValueError("User with this email already exists")

        # Create new user entity
        new_user = {
            "email": user_create_dto.email,
            "password": user_create_dto.password  # In real scenarios, hash the password
        }

        # Save the new user to the repository
        created_user = self.user_repository.create(new_user)

        return created_user