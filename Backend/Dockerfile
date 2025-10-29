FROM python:3.13-slim

WORKDIR /app

# Instalar uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Instalar dependencias del sistema necesarias para psycopg2 y cffi
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libffi-dev \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de dependencias
COPY Backend/pyproject.toml Backend/uv.lock* ./
COPY README.md ./
# Instalar dependencias usando uv
RUN uv sync --frozen --no-dev

# Copiar el código de la aplicación
COPY Backend/ ./

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uv", "run", "fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]