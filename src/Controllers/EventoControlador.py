from sqlalchemy.orm import Session
from Schemas.Eventoschema import EventoCrearSchema
from Services.EventoServicio import crear_evento, buscar_evento, buscar_evento_por_nombre, buscar_evento_por_fechas, buscar_evento_por_lugar, eliminar_evento, actualizar_evento, listar_eventos, buscar_evento_por_estados
from datetime import datetime

def crear_evento_controlador(db: Session, evento: EventoCrearSchema):
    return crear_evento(db, evento)

def listar_eventos_controlador(db: Session):
    return listar_eventos(db)

def buscar_evento_controlador(db: Session, id: str):
    return buscar_evento(db, id)

def buscar_evento_por_nombre_controlador(db: Session, nombre: str):
    return buscar_evento_por_nombre(db, nombre)

def buscar_evento_por_fechas_controlador(db: Session, fecha: datetime):
    return buscar_evento_por_fechas(db, fecha)

def buscar_eventos_por_estados(db: Session, id_estado: int):
    return buscar_evento_por_estados(db, id_estado)

def buscar_evento_por_lugar_controlador(db: Session, lugar: str):
    return buscar_evento_por_lugar(db, lugar)

def eliminar_evento_controlador(db: Session, id: str):
    return eliminar_evento(db, id)

def actualizar_evento_controlador(db: Session, id_evento: str, evento: EventoCrearSchema):
    return actualizar_evento(db, id_evento, evento)