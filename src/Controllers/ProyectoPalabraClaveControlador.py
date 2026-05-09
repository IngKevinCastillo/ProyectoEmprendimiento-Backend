from sqlalchemy.orm import Session
from Services.ProyectoPalabraClaveServicio import actualizar_proyecto_palabra_clave, buscar_proyecto_palabra_clave, crear_proyecto_palabra_clave, elimina_proyecto_palabra_clave, listar_proyecto_palabra_clave
from Schemas.ProyectoPalabraClaveSchema import ProyectoPalabraClaveCrearSchema, ProyectoPalabraClaveActualizarSchema

def crear_proyecto_palabra_clave_controlador(db: Session, proyecto_palabra_clave: ProyectoPalabraClaveCrearSchema):
    return crear_proyecto_palabra_clave(db, proyecto_palabra_clave)

def buscar_proyecto_palabra_clave_controlador(db: Session, id_proyecto_palabra_clave: int):
    return buscar_proyecto_palabra_clave(db, id_proyecto_palabra_clave)

def listar_proyecto_palabra_clave_controlador(db: Session, id_proyecto: int):
    return listar_proyecto_palabra_clave(db, id_proyecto)

def actualizar_proyecto_palabra_clave_controlador(db: Session, id_proyecto_palabra_clave: int, proyecto_palabra_clave: ProyectoPalabraClaveActualizarSchema):
    return actualizar_proyecto_palabra_clave(db, id_proyecto_palabra_clave, proyecto_palabra_clave)

def elimina_proyecto_palabra_clave_controlador(db: Session, id_proyecto_palabra_clave: int):
    return elimina_proyecto_palabra_clave(db, id_proyecto_palabra_clave)