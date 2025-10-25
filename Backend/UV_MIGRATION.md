# Migración a UV - Comandos y Workflow

## ✅ Migración Completada

Se ha migrado exitosamente de `pip + requirements.txt` a **uv + pyproject.toml**.

## 📦 Gestión de Dependencias

### Instalar dependencias
```bash
# Instalar todas las dependencias (producción + desarrollo)
uv sync --group dev

# Solo dependencias de producción
uv sync

# Instalar nueva dependencia
uv add fastapi
uv add pytest --group dev  # Dependencia de desarrollo
```

### Actualizar dependencias
```bash
# Actualizar todas
uv sync --upgrade

# Actualizar una específica
uv add fastapi@latest
```

## 🚀 Comandos Principales

### Desarrollo
```bash
# Ejecutar servidor en modo desarrollo
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Ejecutar tests
uv run pytest tests/unit/ -v

# Tests con cobertura
uv run pytest tests/unit/ --cov=presentation --cov=application --cov=domain --cov=infrastructure --cov-report=html

# Tests en modo watch (recarga automática)
uv run pytest-watch tests/unit/ -- -v

# Linting y formato
uv run ruff check .         # Verificar código
uv run ruff check --fix .   # Corregir automáticamente
uv run ruff format .        # Formatear código
```

### Base de Datos
```bash
# Migrar base de datos
uv run alembic upgrade head

# Rollback última migración
uv run alembic downgrade -1

# Crear nueva migración
uv run alembic revision --autogenerate
```

### Producción
```bash
# Ejecutar servidor en producción
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

## 📁 Estructura de Dependencias

### Dependencias de Producción
- **FastAPI**: Framework web principal
- **SQLAlchemy/SQLModel**: ORM y base de datos
- **Pydantic**: Validación de datos
- **Authentication**: JWT, OAuth, bcrypt
- **HTTP clients**: httpx, requests
- **Utilities**: python-dotenv, pyyaml, click

### Dependencias de Desarrollo
- **Testing**: pytest, coverage, pytest-watch
- **Code Quality**: ruff (linting + formatting)

## 🔄 Comandos de Equivalencia

| Comando Anterior (pip) | Comando Nuevo (uv) |
|------------------------|---------------------|
| `pip install -r requirements.txt` | `uv sync --group dev` |
| `pip install package` | `uv add package` |
| `pip install --dev package` | `uv add package --group dev` |
| `python -m pytest` | `uv run pytest tests/unit/ -v` |
| `uvicorn main:app --reload` | `uv run uvicorn main:app --reload` |

## 🏗️ Estructura del Proyecto

```
pyproject.toml          # ✅ Configuración principal
├── [project]           # Metadatos del proyecto
├── dependencies        # Dependencias de producción
├── [dependency-groups] # Dependencias de desarrollo
├── [tool.uv.scripts]   # Scripts personalizados
└── [tool.hatch.build]  # Configuración de build
```

## 🔧 Ventajas de UV

1. **Velocidad**: Resolución e instalación muy rápida
2. **Lockfile**: Reproducibilidad garantizada (`uv.lock`)
3. **Scripts**: Comandos personalizados fáciles
4. **Grupos**: Organización clara de dependencias
5. **Compatibilidad**: 100% compatible con pip/PyPI

## 📋 Próximos Pasos

1. **Eliminar `requirements.txt`**: Ya no es necesario
2. **Actualizar CI/CD**: Cambiar a comandos `uv`
3. **Documentar equipo**: Compartir nuevos comandos
4. **Configurar IDE**: Actualizar path del intérprete

## 🚨 Importante

- El archivo `uv.lock` **debe** estar en el repositorio
- Usar `uv run` para ejecutar comandos Python
- Las dependencias están ahora en `pyproject.toml`
- El virtual environment se gestiona automáticamente