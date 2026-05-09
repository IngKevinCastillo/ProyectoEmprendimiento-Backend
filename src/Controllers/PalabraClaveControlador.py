from sqlalchemy.orm import Session
from Services.PalabraClaveServicio import actualizar_palabra_clave, buscar_palabra_clave, buscar_palabra_clave_palabra, crear_palabra_clave, listar_palabras_clave
from Schemas.PalabraClaveSchema import PalabraClaveCrearSchema, PalabraClaveActualizarSchema

def crear_palabra_clave_controlador(db: Session, palabra_clave: PalabraClaveCrearSchema):
    return crear_palabra_clave(db, palabra_clave)

def buscar_palabra_clave_controlador(db: Session, id_palabra_clave: int):
    return buscar_palabra_clave(db, id_palabra_clave)

def buscar_palabra_clave_palabra_controlador(db: Session, palabra: str):
    return buscar_palabra_clave_palabra(db, palabra)

def listar_palabras_clave_controlador(db: Session):
    return listar_palabras_clave(db)

def actualizar_palabra_clave_controlador(db: Session, id_palabra_clave: int, palabra_clave: PalabraClaveActualizarSchema):
    return actualizar_palabra_clave(db, id_palabra_clave, palabra_clave)