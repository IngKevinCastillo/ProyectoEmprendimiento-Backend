from sqlalchemy.orm import Session
from Schemas.Eventoschema import EventoCrearSchema
from Services.EventoServicio import cambiar_estado, buscar_evento_por_rango_fechas, crear_evento, buscar_evento, buscar_evento_por_nombre, buscar_evento_por_fecha, buscar_evento_por_lugar, eliminar_evento, actualizar_evento, listar_eventos, buscar_evento_por_estados
from datetime import datetime, date
from Schemas.EstadosSchema import CambiarEstado

def crear_evento_controlador(db: Session, evento: EventoCrearSchema):
    return crear_evento(db, evento)

def listar_eventos_controlador(db: Session):
    return listar_eventos(db)

def buscar_evento_controlador(db: Session, id: int):
    return buscar_evento(db, id)

def buscar_evento_por_nombre_controlador(db: Session, nombre: str):
    return buscar_evento_por_nombre(db, nombre)

def buscar_evento_por_fecha_controlador(db: Session, fecha: datetime):
    return buscar_evento_por_fecha(db, fecha)

def buscar_evento_por_rango_fechas_controlador(db: Session, fecha_inicio: date, fecha_fin: date):
    return buscar_evento_por_rango_fechas(db, fecha_inicio, fecha_fin)

def buscar_eventos_por_estados(db: Session, id_estado: int):
    return buscar_evento_por_estados(db, id_estado)

def buscar_evento_por_lugar_controlador(db: Session, lugar: str):
    return buscar_evento_por_lugar(db, lugar)

def eliminar_evento_controlador(db: Session, id: int):
    return eliminar_evento(db, id)

def actualizar_evento_controlador(db: Session, id_evento: int, evento: EventoCrearSchema):
    return actualizar_evento(db, id_evento, evento)

def cambiar_estado_controlador(db: Session, id_evento: int, estado: CambiarEstado):
    return cambiar_estado(db, id_evento, estado)