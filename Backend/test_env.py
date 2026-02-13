#!/usr/bin/env python3
"""
Script de prueba para verificar que las variables de entorno se cargan correctamente
"""

from src.config import settings

def test_env_loading():
    print("🔧 Verificando carga de variables de entorno...")
    print(f"JWT_SECRET_KEY: {'✅ Cargada' if settings.JWT_SECRET_KEY else '❌ No encontrada'}")
    print(f"JWT_ALGORITHM: {settings.JWT_ALGORITHM}")
    print(f"JWT_ACCESS_TOKEN_EXPIRE_HOURS: {settings.JWT_ACCESS_TOKEN_EXPIRE_HOURS}")
    print(f"JWT_REFRESH_TOKEN_EXPIRE_DAYS: {settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS}")
    print(f"DATABASE_URL: {'✅ Cargada' if settings.DATABASE_URL else '❌ No encontrada'}")
    
    if settings.JWT_SECRET_KEY:
        print("🎉 ¡Configuración cargada exitosamente!")
    else:
        print("⚠️ Hay problemas con la configuración")

if __name__ == "__main__":
    test_env_loading()