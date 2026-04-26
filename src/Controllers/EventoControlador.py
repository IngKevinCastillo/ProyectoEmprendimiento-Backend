from sqlalchemy.orm import Session
from Schemas.Eventoschema import EventoCrearSchema
from Services.EventoServicio import crear_evento, buscar_evento, buscar_evento_por_nombre, buscar_evento_por_fechas, buscar_evento_por_lugar, eliminar_evento, actualizar_evento
from datetime import datetime

def crear_evento_controlador(db: Session, evento: EventoCrearSchema):
    return crear_evento(db, evento)

def buscar_evento_controlador(db: Session, id: int):
    return buscar_evento(db, id)

def buscar_evento_por_nombre_controlador(db: Session, nombre: str):
    return buscar_evento_por_nombre(db, nombre)

def buscar_evento_por_fechas_controlador(db: Session, fecha: datetime):
    return buscar_evento_por_fechas(db, fecha)

def buscar_evento_por_lugar_controlador(db: Session, lugar: str):
    return buscar_evento_por_lugar(db, lugar)

def eliminar_evento_controlador(db: Session, id: int):
    return eliminar_evento(db, id)

def actualizar_evento_controlador(db: Session, evento: EventoCrearSchema):
    return actualizar_evento(db, evento)