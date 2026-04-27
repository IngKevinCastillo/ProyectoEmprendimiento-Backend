from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.EventoModelo import EventoModelo
from Schemas.Eventoschema import EventoCrearSchema
from Utils.Mapeadorutilidades import auto_mapear
from datetime import datetime

def crear_evento(db: Session, evento: EventoCrearSchema):
    nuevo_evento = EventoModelo(
        nombre_evento=evento.nombre_evento,
        tipo_evento=evento.tipo_evento,
        fecha=evento.fecha,
        lugar=evento.lugar
    )
    db.add(nuevo_evento)
    db.commit()
    db.refresh(nuevo_evento)
    return nuevo_evento

def listar_eventos(db: Session):
    return db.query(EventoModelo).all()

def buscar_evento(db: Session, id: str):
    return db.query(EventoModelo).filter(EventoModelo.id_evento == int(id)).first()

def buscar_evento_por_nombre(db: Session, nombre: str):
    return db.query(EventoModelo).filter(EventoModelo.nombre_evento == nombre).first()

def buscar_evento_por_fechas(db: Session, fecha: datetime):
    return db.query(EventoModelo).filter(EventoModelo.fecha == fecha).all()

def buscar_evento_por_lugar(db: Session, lugar: str):
    return db.query(EventoModelo).filter(EventoModelo.lugar == lugar).all()

def eliminar_evento(db:Session, id: str):
    existente = buscar_evento(db, int(id))
    if not existente:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    db.delete(existente)
    db.commit()
    return {"message": "Evento eliminado correctamente"}

def actualizar_evento( db: Session, id_evento: str, evento: any):
    existente = buscar_evento(db, int(id_evento))
    if not existente:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    
    auto_mapear(existente, evento, excluir=["id_evento"])

    db.commit()
    db.refresh(existente)
    return existente