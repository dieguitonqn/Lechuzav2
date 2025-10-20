#!/usr/bin/env python3
"""
Script para actualizar todos los imports después de la reorganización según Clean Architecture
"""

import os
import re
from pathlib import Path

# Mapeo de las rutas antiguas a las nuevas
IMPORT_MAPPINGS = {
    # Models -> Domain Entities
    r'from models\.': 'from domain.entities.',
    r'import models\.': 'import domain.entities.',
    
    # Core interfaces -> Domain interfaces
    r'from core\.interfaces\.': 'from domain.interfaces.',
    r'import core\.interfaces\.': 'import domain.interfaces.',
    
    # Core use_cases -> Application use_cases
    r'from core\.use_cases\.': 'from application.use_cases.',
    r'import core\.use_cases\.': 'import application.use_cases.',
    
    # Core dtos -> Application dtos
    r'from core\.dtos\.': 'from application.dtos.',
    r'import core\.dtos\.': 'import application.dtos.',
    
    # Database -> Infrastructure database
    r'from database\.': 'from infrastructure.database.',
    r'import database\.': 'import infrastructure.database.',
    
    # API -> Presentation API
    r'from api\.': 'from presentation.api.',
    r'import api\.': 'import presentation.api.',
    
    # Routers -> Presentation routers
    r'from routers\.': 'from presentation.routers.',
    r'import routers\.': 'import presentation.routers.',
}

def update_imports_in_file(file_path):
    """Actualiza los imports en un archivo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Aplicar todas las transformaciones
        for old_pattern, new_replacement in IMPORT_MAPPINGS.items():
            content = re.sub(old_pattern, new_replacement, content)
        
        # Solo escribir si hubo cambios
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Actualizado: {file_path}")
            return True
        else:
            print(f"⏭️  Sin cambios: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error en {file_path}: {e}")
        return False

def main():
    """Función principal"""
    backend_path = Path(__file__).parent
    updated_files = 0
    total_files = 0
    
    # Procesar todos los archivos .py
    for py_file in backend_path.rglob("*.py"):
        # Excluir archivos en directorios específicos
        if any(exclude in str(py_file) for exclude in ['__pycache__', 'venv', '.pytest_cache']):
            continue
            
        # Excluir este mismo script
        if py_file.name == 'update_imports.py':
            continue
            
        total_files += 1
        if update_imports_in_file(py_file):
            updated_files += 1
    
    print(f"\n📊 Resumen:")
    print(f"   Archivos procesados: {total_files}")
    print(f"   Archivos actualizados: {updated_files}")
    print(f"   Archivos sin cambios: {total_files - updated_files}")

if __name__ == "__main__":
    main()