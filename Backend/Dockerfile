FROM python:3.12-slim

WORKDIR /app

# Instalar uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copiar archivos de dependencias
COPY Backend/pyproject.toml Backend/uv.lock* ./
COPY Backend/uv.lock ./
COPY README.md ./
# Instalar dependencias usando uv
RUN uv sync --frozen --no-dev

# Copiar el código de la aplicación
COPY Backend/ ./

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uv", "run", "fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]