import os
from pathlib import Path
from src.modules.documents.application.dtos import DocumentToSaveFile
from src.domain.entities.users import User


class DocumentsFilesRepo:
    def __init__(self):
        # Aquí podrías inicializar cualquier recurso necesario, como una conexión a la base de datos
        pass

    async def save_file(self, doc_file:DocumentToSaveFile, user: User, dirpath: Path) -> str:
        # Aquí iría la lógica para guardar el archivo en el sistema de archivos o en un servicio de almacenamiento
        sanitized_filename = f"{doc_file.codigo}_{doc_file.revision}_{doc_file.descripcion}.pdf"
        sanitized_filename = sanitized_filename.replace(" ", "_")
        file_path = os.path.join(dirpath, sanitized_filename)
        try:
            with open(file_path, "wb") as f:
                content = await doc_file.file.read()
                f.write(content)
        except OSError as e:
            raise RuntimeError(f"Error writing file {file_path}: {e}")
        return file_path
        