import os
import jwt
from datetime import datetime, timedelta, timezone
from typing import Optional
from sqlmodel import Session, select
from pwdlib import PasswordHash
from dotenv import load_dotenv

from src.modules.auth.domain.interfaces.auth_interface import IAuthRepository
from src.modules.auth.domain.entities.auth_token import AuthToken, AuthUser
from src.domain.entities.users import User  # Asumiendo que existe la entidad User en el dominio principal

# Cargar variables de entorno
load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_HOURS = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_HOURS", "24"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_DAYS", "7"))


password_hash = PasswordHash.recommended()


class AuthRepository(IAuthRepository):
    def __init__(self, db: Session, secret_key: str = SECRET_KEY):
        self.db = db
        self.secret_key = secret_key

    async def authenticate_user(self, email: str, password: str) -> Optional[AuthToken]:
        """
        Authenticate user with email and password
        """
        try:
            # Find user by email
            statement = select(User).where(User.email == email)
            result = self.db.exec(statement)
            user_db = result.first()

            if not user_db:
                print(f"No user found with email: {email}")
                return None

            # Verify password
            if not password_hash.verify(password, user_db.password_hash):
                print(f"Invalid password for email: {email}")
                return None

            # Generate tokens
            access_token = self._generate_access_token(user_db)
            refresh_token = self._generate_refresh_token(user_db)

            # Create user object
            user = AuthUser(
                id=user_db.id,
                name=user_db.nombre_completo or user_db.email,
                email=user_db.email,
                role=self._get_user_role(user_db)
            )

            return AuthToken(
                access_token=access_token,
                refresh_token=refresh_token,
                token_type="Bearer",
                user=user
            )

        except Exception as e:
            print(f"Error authenticating user: {e}")
            return None

    async def refresh_token(self, refresh_token: str) -> Optional[AuthToken]:
        """
        Refresh access token using refresh token
        """
        try:
            # Decode refresh token
            payload = jwt.decode(refresh_token, self.secret_key, algorithms=[ALGORITHM])
            user_id = payload.get("sub")

            if not user_id:
                return None

            # Find user by ID
            statement = select(User).where(User.id == user_id)
            result = self.db.exec(statement)
            user_db = result.first()

            if not user_db:
                return None

            # Generate new tokens
            access_token = self._generate_access_token(user_db)
            print(f"Generated access token: {access_token}")
            new_refresh_token = self._generate_refresh_token(user_db)

            # Create user object
            user = AuthUser(
                id=user_db.id,
                name=user_db.nombre_completo or user_db.email,
                email=user_db.email,
                role=self._get_user_role(user_db)
            )

            return AuthToken(
                access_token=access_token,
                refresh_token=new_refresh_token,
                token_type="Bearer",
                user=user
            )

        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
        except Exception as e:
            print(f"Error refreshing token: {e}")
            return None

    def _generate_access_token(self, user:User) -> str:
        """
        Generate access token for user
        """
        expiry = datetime.now(timezone.utc) + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
        payload = {
            "sub": str(user.id),
            "email": user.email,
            "exp": expiry,
            "iat": datetime.now(timezone.utc),
            "type": "access"
        }
        print(f"Generating access token for user {user.email} with payload: {payload}")
        return jwt.encode(payload, self.secret_key, algorithm=ALGORITHM)

    def _generate_refresh_token(self, user:User) -> str:
        """
        Generate refresh token for user
        """
        expiry = datetime.now(timezone.utc) + timedelta(days=7)
        payload = {
            "sub": str(user.id),
            "email": user.email,
            "exp": expiry,
            "iat": datetime.now(timezone.utc),
            "type": "refresh"
        }
        return jwt.encode(payload, self.secret_key, algorithm=ALGORITHM)

    def _get_user_role(self, user:User) -> str:
        """
        Determine user role based on user attributes
        """
        if hasattr(user, 'is_admin') and user.is_admin:
            return "admin"
        elif hasattr(user, 'is_epen_user') and user.is_epen_user:
            return "epen_user"
        else:
            return "user"