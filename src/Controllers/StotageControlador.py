from Services import StorageServicio
from sqlalchemy.orm import Session

def subir_foto_controlador(archivo: bytes, nombre_archivo: str):
    return StorageServicio.subir_foto(archivo, nombre_archivo)

def eliminar_foto_controlador(foto_url: str):
    return StorageServicio.eliminar_foto(foto_url)