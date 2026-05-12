from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.EventoModelo import EventoModelo
from Schemas.Eventoschema import EventoCrearSchema
from Utils.Mapeadorutilidades import auto_mapear
from datetime import datetime, date
from typing import Final
from Schemas.EstadosSchema import CambiarEstado

ESTADO_ELIMINADO: Final = 6
ESTADO_ACTIVO: Final = 8

def crear_evento(db: Session, evento: EventoCrearSchema):
    existente = buscar_evento_por_nombre(db, evento.nombre_evento)
    
    if existente:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El evento especificado ya existe.")
    
    if(existente.id_estado == ESTADO_ELIMINADO):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El estado especificado no existe.")
    
    nuevo_evento = EventoModelo(
        nombre_evento=evento.nombre_evento,
        tipo_evento=evento.tipo_evento,
        fecha=evento.fecha,
        lugar=evento.lugar,
        descripcion=evento.descripcion,
        id_estado=ESTADO_ACTIVO
    )
    db.add(nuevo_evento)
    db.commit()
    db.refresh(nuevo_evento)
    return nuevo_evento

def listar_eventos(db: Session):
    existentes = db.query(EventoModelo).filter(EventoModelo.id_estado != ESTADO_ELIMINADO).all()
    
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existen eventos")
    
    return existentes

def buscar_evento(db: Session, id: int):
    existente = db.query(EventoModelo).filter(EventoModelo.id_evento == id, EventoModelo.id_estado != ESTADO_ELIMINADO).first()
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El evento especificado no existe.")
    
    return existente

def buscar_evento_por_nombre(db: Session, nombre: str):
    existente = db.query(EventoModelo).filter(EventoModelo.nombre_evento == nombre, EventoModelo.id_estado != ESTADO_ELIMINADO).first()
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El evento especificado no existe.")
    
    return existente

def buscar_evento_por_fecha(db: Session, fecha: datetime):
    existentes = db.query(EventoModelo).filter(EventoModelo.fecha == fecha, EventoModelo.id_estado != ESTADO_ELIMINADO).all()
    
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existen eventos")
    
    return existentes

def buscar_evento_por_rango_fechas(db: Session, fecha_inicio: date, fecha_fin: date):
    existentes = db.query(EventoModelo).filter(
        EventoModelo.fecha_inicio >= fecha_inicio,
        EventoModelo.fecha_fin <= fecha_fin,
        EventoModelo.id_estado != ESTADO_ELIMINADO
    ).all()
    
    if not existentes:
        raise HTTPException(status_code=404, detail="No existen eventos en ese rango de fechas")
    
    return existentes

def buscar_evento_por_estados(db: Session, id_estado: int):
    existentes = db.query(EventoModelo).filter(EventoModelo.id_estado == id_estado).all()
    
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existen eventos")
    
    return existentes

def buscar_evento_por_lugar(db: Session, lugar: str):
    existentes = db.query(EventoModelo).filter(EventoModelo.lugar == lugar, EventoModelo.id_estado != ESTADO_ELIMINADO).all()
    
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existen eventos")
    
    return existentes

def eliminar_evento(db:Session, id: int):
    existente = buscar_evento(db, id)

    existente.id_estado = ESTADO_ELIMINADO

    db.commit()
    db.refresh(existente)
    return {"message": "Evento eliminado correctamente"}

def actualizar_evento( db: Session, id_evento: int, evento: any):
    existente = buscar_evento(db, id_evento)
    
    auto_mapear(existente, evento, excluir=["id_evento", "id_estado"])

    db.commit()
    db.refresh(existente)
    return 

def cambiar_estado(db: Session, id_evento: int, estado: CambiarEstado):
    existente = db.query(EventoModelo).filter(
        EventoModelo.id_evento == id_evento
    ).first()
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El evento especificado no existe.")
    
    existente.id_estado = estado.id_estado_cambiar
    
    db.commit()
    db.refresh(existente)
    return existente