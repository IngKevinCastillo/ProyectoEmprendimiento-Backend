from Services import FotosServicio

def subir_foto_controlador(archivo: bytes, nombre_archivo: str):
    return FotosServicio.subir_foto(archivo, nombre_archivo)