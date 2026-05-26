from Services import StorageServicio
from sqlalchemy.orm import Session

def subir_foto_controlador(archivo: bytes, nombre_archivo: str):
    return StorageServicio.subir_foto(archivo, nombre_archivo)

def eliminar_foto_controlador(foto_url: str):
    return StorageServicio.eliminar_foto(foto_url)

def subir_pdf(archivo: bytes, nombre_archivo: str) -> str:
    return StorageServicio.subir_pdf(archivo, nombre_archivo)

def eliminar_pdf(pdf_url: str):
    return StorageServicio.eliminar_pdf(pdf_url)