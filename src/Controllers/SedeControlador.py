from sqlalchemy.orm import Session
from Services.SedeServicio import obtener_sede_servicio, obtener_sedes_servicio, obtener_sede_por_nombre_servicio

def obtener_sede_controlador(db: Session, id_sede: str):
    return obtener_sede_servicio(db, id_sede)

def obtener_sede_por_nombre_controlador(db: Session, nombre: str):
    return obtener_sede_por_nombre_servicio(db, nombre)

def listar_sedes_controlador(db: Session):
    return obtener_sedes_servicio(db)