from sqlalchemy.orm import Session
from Services.SedeServicio import crear_sede_servicio, obtener_sede_servicio, actualizar_sede_servicio, eliminar_sede_servicio, obtener_sedes_servicio, obtener_sede_por_nombre_servicio
from Schemas.SedeSchemas import SedeCrearSchema, SedeActualizarSchema 

def crear_sede_contolador(db: Session, sede: SedeCrearSchema):
    return crear_sede_servicio(db, sede)

def obtener_sede_controlador(db: Session, id_sede: str):
    return obtener_sede_servicio(db, id_sede)

def obtener_sede_por_nombre_controlador(db: Session, nombre: str):
    return obtener_sede_por_nombre_servicio(db, nombre)

def actualizar_sede_controlador(db: Session, id_sede: str, sede: SedeActualizarSchema):
    return actualizar_sede_servicio(db, id_sede, sede)

def eliminar_sede_controlador(db: Session, id_sede: str):
    return eliminar_sede_servicio(db, id_sede)

def listar_sedes_controlador(db: Session):
    return obtener_sedes_servicio(db)