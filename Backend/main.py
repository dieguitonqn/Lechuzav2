from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from sqlmodel import Session, select
from models import User
from database import create_db_and_tables, engine
from routers import users, auth
from routers.auth import crypt



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create the database and tables at startup
    print ("Creating database and tables...")
    
    create_db_and_tables()
    with Session(engine) as session:
    
    
        # 3. Verificamos si el usuario administrador por defecto ya existe.
        # Esto evita el error de UniqueViolation al reiniciar la aplicación.
        # statement = select(User).where(User.email == "admin@email.com")
        # existing_admin = session.exec(statement).first()

        # # 4. Si el usuario NO existe, lo creamos.
        # # Esta es la corrección principal, la condición `if not existing_admin`.
        # if not existing_admin:
        #     print("Creando usuario administrador por defecto...")

        #     # Es crucial hashear la contraseña antes de guardarla.
        #     # `hash_password` es una función asumida.
        #     # hashed_password = hash_password("admin-password")

        #     user_admin_default = User(
        #         name="Admin",
        #         email="admin@email.com",
        #         google_id="admin-google-id",
        #         # Guarda la contraseña hasheada, no en texto plano.
        #         # password="$2y$12$Xqb.PwbPpnzqxJ/tAKEnruwkPDuq7fAUu8TzhY28uL/iN6KjEa1Gi", #admin-password
        #         password=crypt.hash("admin-password"),  # Hasheamos la contraseña
        #         is_active=True,
        #         is_verified=True,
        #         is_admin=True
        #     )

        #     # 5. Lo agregamos a la sesión y hacemos commit para guardarlo en la DB.
        #     session.add(user_admin_default)
        #     session.commit()

        #     # 6. Refrescamos el objeto para obtener su ID y otros valores por defecto.
        #     session.refresh(user_admin_default)

        #     print(f"Usuario administrador por defecto creado: {user_admin_default.email}")
        # else:
        #     print("El usuario administrador por defecto ya existe. Omitiendo la creación.")

        yield #Yield es para que FastAPI pueda iniciar y ejecutar la aplicación
    # Here you could add any cleanup code if needed



app = FastAPI(lifespan=lifespan)

# Routers
app.include_router(users.users, prefix="/api", tags=["users"])
app.include_router(auth.router, prefix="/api", tags=["auth"])

# Configuración de CORS
origins = [
    "http://localhost:3000",  # Tu frontend Next.js
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Lista específica de orígenes permitidos
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["Set-Cookie"],  # Importante para manejar cookies
)

# Main endpoint
@app.get("/")
def main():
    return {"message": "Hello World"}