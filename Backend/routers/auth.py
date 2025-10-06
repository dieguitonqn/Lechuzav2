from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response, status, Cookie, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlmodel import Session, select
from models.users import User, UserCreate
from Backend.database.database import get_session

from fastapi.security import OAuth2PasswordBearer
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from fastapi_nextauth_jwt import NextAuthJWT
# from jose import jwt, jwe, JWTError, JWSError, ExpiredSignatureError


router = APIRouter()

class Cookie(BaseModel):
    access_token: str | None = None

oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")


crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"
SECRET_KEY = "secreta_posta"
AUTH_SECRET="vgzX25nZEv0di8k5vV8XyPjFGDUaMS1DOs5IncjtmRc="
TOKEN_EXPIRATION_TIME = timedelta(minutes=1)

JWT = NextAuthJWT(
    secret=AUTH_SECRET,
)



async def verify_password(user: User, password: str):
    print(f"Verifying password for user: {user.email}")
    print(f"User password: {user.password}")
    if user.password is None:
        return False
    
    return crypt.verify(password, user.password)

async def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        utc_minus_3 = timezone(timedelta(hours=-3))
        expire = datetime.now(tz=utc_minus_3) + TOKEN_EXPIRATION_TIME
    to_encode.update({"exp": expire})
    print(f"Creating access token with data: {to_encode}")
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def create_encrypted_password(password: str):
    print(f"Creating encrypted password for: {password}")
    if not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password cannot be empty"
        )

    return crypt.hash(password)


async def get_user(token: str = Depends(oauth2), session: Session = Depends(get_session)):
    try:        
        decoded_token = jwt.decode(
            token, 
            SECRET_KEY, 
            algorithms=[ALGORITHM],
            options={"verify_exp": True}  # Verificar explícitamente la expiración
        )
        if "sub" not in decoded_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token missing subject claim"
            )
            
        user_email = decoded_token["sub"]
        statement = select(User).where(User.email == user_email)
        user = session.exec(statement).first()
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )
           
        return user
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
        )
    except Exception as e:
        print(f"Unexpected error: {str(e)}")  # Debug
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.post("/auth/login")
async def login(response:Response, user:UserCreate , session: Session = Depends(get_session)):
    user_email = user.email
    user_password = user.password

    print(f"Attempting to log in user: {user_email}")
    print(f"User password: {user_password}")
    statement = select(User).where(User.email == user_email)
    user = session.exec(statement).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Invalid authentication credentials")

    # if not user.is_active:
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN, 
    #         detail="Inactive user")

    # Como el usuario existe, genero un token JWT
    if not await verify_password(user, user_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid authentication password")


    # access_token = await create_access_token(data={"sub": user.email})
    # response.set_cookie(
    #     key="access_token",
    #     value=access_token,
    #     httponly=True,
    #     secure=False,  # Cambiar a True en producción
    #     samesite="Lax",
        
    # )
    return user

@router.get ("/auth/mw", status_code=status.HTTP_200_OK)
async def return_mw(
        # resp:Response, 
        # Cookie: Annotated[str, Cookie()], 
        jwt_token:Annotated[dict, Depends(JWT)],
        session: Session = Depends(get_session)
        ):
    print(f"EL jwt es: {jwt_token}")
    # if not Cookie:
    #     raise HTTPException(status_code=401, detail="Token not provided")
    # print(f"Access token received: {Cookie}")

    email = jwt_token.get("email")
    print(f"Email from token: {email}")
    statement = select(User).where(User.email == email)
    user = session.exec(statement).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # new_access_token = await create_access_token(data={"sub": user.email})
    # resp.set_cookie(
    #     key="access_token",
    #     value=new_access_token,
    #     httponly=True,
    #     secure=False,
    #     samesite="Lax",
    # )

    return {
        # "email": user.email,
        # "is_active": user.is_active,
        # "is_admin": user.is_admin
        "prueba":"todo ok"
    }