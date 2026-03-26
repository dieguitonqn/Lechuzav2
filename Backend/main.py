from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from sqlmodel import Session, select
from src.infrastucture.database.database import create_db_and_tables, engine
from passlib.context import CryptContext
from src.domain.entities.users import User
from src.domain.entities.statuses import Status
from src.domain.entities.projects import Project
from src.domain.entities.documents import Document
from src.domain.entities.models_links import ProjectUserLink
from src.domain.entities.companies import Company
from src.modules.routers import module_routers
from pwdlib import PasswordHash


crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")
argon2_hash = PasswordHash("argon2").recommended()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create the database and tables at startup
    print("Creating database and tables...")

    create_db_and_tables()
    with Session(engine) as session:
        # 3. Verificamos si el usuario administrador por defecto ya existe.
        # Esto evita el error de UniqueViolation al reiniciar la aplicación.
        statement = select(User).where(User.email == "admin@email.com")
        existing_admin = session.exec(statement).first()

        # # 4. Si el usuario NO existe, lo creamos.
        # # Esta es la corrección principal, la condición `if not existing_admin`.
        if not existing_admin:
            print("Creando usuario administrador por defecto...")

            # Es crucial hashear la contraseña antes de guardarla.
            # `hash_password` es una función asumida.
            # hashed_password = hash_password("admin-password")

            user_admin_default = User(
                name="Admin",
                email="admin@email.com",
                # Guarda la contraseña hasheada, no en texto plano.
                # password="$2y$12$Xqb.PwbPpnzqxJ/tAKEnruwkPDuq7fAUu8TzhY28uL/iN6KjEa1Gi", #admin-password
                password_hash=argon2_hash.hash(
                    "admin-password"
                ),  # Hasheamos la contraseña
                is_active=True,
                is_verified=True,
                is_admin=True,
            )

            # 5. Lo agregamos a la sesión y hacemos commit para guardarlo en la DB.
            session.add(user_admin_default)
            session.commit()

            # 6. Refrescamos el objeto para obtener su ID y otros valores por defecto.
            session.refresh(user_admin_default)

            print(
                f"Usuario administrador por defecto creado: {user_admin_default.email}"
            )
        else:
            print(
                "El usuario administrador por defecto ya existe. Omitiendo la creación."
            )
        admin_user = existing_admin or user_admin_default
        default_status = Status(
            nombre="EN REVISION",
            descripcion="Documento en proceso de revisión",
        )
        # Verificar si el estado por defecto ya existe
        statement = select(Status).where(Status.nombre == default_status.nombre)
        existing_status = session.exec(statement).first()
        if not existing_status:
            session.add(default_status)
            session.commit()
            session.refresh(default_status)
            print(f"Estado por defecto creado: {default_status.nombre}")
        else:
            print("El estado por defecto ya existe. Omitiendo la creación.")
        status_for_docs = existing_status or default_status
        # ---------------------------------------------------------------------------------------------
        # -----------------------EMPRESA DEFECTO-----------------------
        default_company = Company(
            nombre="EPEN",
            descripcion="Ente Provincial de Energía del Neuquén.",
            codigo="Empresa",
        )
        # Verificar si la empresa por defecto ya existe
        statement = select(Company).where(Company.nombre == default_company.nombre)
        existing_company = session.exec(statement).first()
        if not existing_company:
            session.add(default_company)
            session.commit()
            session.refresh(default_company)
            print(f"Empresa por defecto creada: {default_company.nombre}")
            company_epen = default_company
        else:
            print("La empresa por defecto ya existe. Omitiendo la creación.")
            company_epen = existing_company

        default_company2 = Company(
            nombre="YPF SA",
            descripcion="Yacimientos Petrolíferos Fiscales Sociedad Anónima.",
            codigo="Contratista",
        )
        # Verificar si la segunda empresa por defecto ya existe
        statement = select(Company).where(Company.nombre == default_company2.nombre)

        existing_company2 = session.exec(statement).first()
        if not existing_company2:
            session.add(default_company2)
            session.commit()
            session.refresh(default_company2)
            print(f"Empresa por defecto creada: {default_company2.nombre}")
            company_ypf = default_company2
        else:
            print("La empresa por defecto ya existe. Omitiendo la creación.")
            company_ypf = existing_company2

        default_company3 = Company(
            nombre="Grupo Oeste",
            descripcion="Grupo Oeste SA.",
            codigo="Sub Contratista",
        )
        # Verificar si la tercera empresa por defecto ya existe
        statement = select(Company).where(Company.nombre == default_company3.nombre)
        existing_company3 = session.exec(statement).first()
        if not existing_company3:
            session.add(default_company3)
            session.commit()
            session.refresh(default_company3)
            print(f"Empresa por defecto creada: {default_company3.nombre}")
        else:
            print("La empresa por defecto ya existe. Omitiendo la creación.")

        # ---------------------------------------------------------------------------------------------
        # -----------------------PROYECTO DEFECTO-----------------------
        default_project = Project(
            nombre="Proyecto por defecto",
            codigo="PRY-001",
            descripcion="Este es un proyecto creado por defecto al iniciar la aplicación.",
            card_color="blue",  # Color específico para este proyecto por defecto
            company_id=company_epen.id,
        )
        # Verificar si el proyecto por defecto ya existe
        statement = select(Project).where(Project.nombre == default_project.nombre)
        existing_project = session.exec(statement).first()
        if not existing_project:
            session.add(default_project)
            session.commit()
            session.refresh(default_project)
            print(f"Proyecto por defecto creado: {default_project.nombre}")
            project_1 = default_project
        else:
            print("El proyecto por defecto ya existe. Omitiendo la creación.")
            project_1 = existing_project

            # ---------------------------------------------------------------------------------------------
        # -----------------------PROYECTO DEFECTO 2-----------------------
        default_project2 = Project(
            nombre="Proyecto por defecto 2",
            codigo="PRY-002",
            descripcion="Este es un segundo proyecto creado por defecto al iniciar la aplicación.",
            company_id=company_ypf.id,
        )
        # Verificar si el proyecto por defecto ya existe
        statement = select(Project).where(Project.nombre == default_project2.nombre)
        existing_project2 = session.exec(statement).first()
        if not existing_project2:
            session.add(default_project2)
            session.commit()
            session.refresh(default_project2)
            print(f"Proyecto por defecto creado: {default_project2.nombre}")
            project_2 = default_project2
        else:
            print("El proyecto por defecto ya existe. Omitiendo la creación.")
            project_2 = existing_project2

        # ---------------------------------------------------------------------------------------------
        # -----------------------DOCUMENTOS DE EJEMPLO-----------------------
        sample_documents = [
            Document(
                codigo="DOC-PRY001-001",
                nombre="Plano General de Instalacion",
                revision="A",
                estado_id=status_for_docs.id,
                project_id=project_1.id,
                ttal_np_id=None,
            ),
            Document(
                codigo="DOC-PRY001-002",
                nombre="Especificacion Tecnica de Materiales",
                revision="B",
                estado_id=status_for_docs.id,
                project_id=project_1.id,
                ttal_np_id=None,
            ),
            Document(
                codigo="DOC-PRY002-001",
                nombre="Memoria de Calculo Estructural",
                revision="A",
                estado_id=status_for_docs.id,
                project_id=project_2.id,
                ttal_np_id=None,
            ),
            Document(
                codigo="DOC-PRY002-002",
                nombre="Procedimiento de Montaje",
                revision="C",
                estado_id=status_for_docs.id,
                project_id=project_2.id,
                ttal_np_id=None,
            ),
        ]

        for sample_document in sample_documents:
            statement = select(Document).where(
                (Document.codigo == sample_document.codigo)
                & (Document.project_id == sample_document.project_id)
            )
            existing_document = session.exec(statement).first()
            if not existing_document:
                session.add(sample_document)
                session.commit()
                session.refresh(sample_document)
                print(f"Documento de ejemplo creado: {sample_document.codigo}")
            else:
                print(
                    f"El documento de ejemplo {sample_document.codigo} ya existe. Omitiendo la creación."
                )
        # ---------------------------------------------------------------------------------------------
        # -----------------------Model Link DEFECTO-----------------------
        if admin_user and project_1:
            # Verificar si el enlace por defecto ya existe
            statement = select(ProjectUserLink).where(
                (ProjectUserLink.project_id == project_1.id)
                & (ProjectUserLink.user_id == admin_user.id)
            )
            existing_link = session.exec(statement).first()
            if not existing_link:
                default_link = ProjectUserLink(
                    project_id=project_1.id,
                    user_id=admin_user.id,
                    can_view_docs=True,
                    can_upload_docs=True,
                    can_correct_docs=True,
                )
                session.add(default_link)
                session.commit()
                print(
                    f"Enlace por defecto creado entre el proyecto '{project_1.nombre}' y el usuario '{admin_user.email}'."
                )
            else:
                print("El enlace por defecto ya existe. Omitiendo la creación.")

            if admin_user and project_2:
                # Verificar si el enlace por defecto ya existe
                statement = select(ProjectUserLink).where(
                    (ProjectUserLink.project_id == project_2.id)
                    & (ProjectUserLink.user_id == admin_user.id)
                )
                existing_link = session.exec(statement).first()
                if not existing_link:
                    default_link = ProjectUserLink(
                        project_id=project_2.id,
                        user_id=admin_user.id,
                        can_view_docs=True,
                        can_upload_docs=True,
                        can_correct_docs=True,
                    )
                    session.add(default_link)
                    session.commit()
                    print(
                        f"Enlace por defecto creado entre el proyecto '{project_2.nombre}' y el usuario '{admin_user.email}'."
                    )
                else:
                    print("El enlace por defecto ya existe. Omitiendo la creación.")

                    

        yield  # Yield es para que FastAPI pueda iniciar y ejecutar la aplicación
    # Here you could add any cleanup code if needed


app = FastAPI(lifespan=lifespan)

# Routers
app.include_router(module_routers, prefix="/api/v1", tags=["v1"])

# app.include_router(users.users, prefix="/api", tags=["users"])
# app.include_router(auth.router, prefix="/api", tags=["auth"])
# app.include_router(company.router, prefix="/api", tags=["company"])
# app.include_router(projects.projects, prefix="/api", tags=["projects"])
# app.include_router(documents.documents, prefix="/api", tags=["documents"])
# app.include_router(ttal_np.ttal_np, prefix="/api", tags=["ttals_nps"])

# Configuración de CORS
origins = [
    "http://localhost:3000",  # Next.js
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Lista específica de orígenes permitidos
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    # expose_headers=["Set-Cookie"],  # Importante para manejar cookies
)

# # Main endpoint
# @app.get("/")
# def main():
#     return {"message": "Hello World"}
