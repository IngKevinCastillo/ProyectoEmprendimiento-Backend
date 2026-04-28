from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.ProyectoModelo import ProyectoModelo

from Utils.Mapeadorutilidades import auto_mapear

def crearEmprendimiento(db: Session, evento: EventoCrearSchema):
    nuevo_evento = ProyectoModelo(
        nombre_evento=evento.nombre_evento,
        tipo_evento=evento.tipo_evento,
        fecha=evento.fecha,
        lugar=evento.lugar
    )
    db.add(nuevo_evento)
    db.commit()
    db.refresh(nuevo_evento)
    return nuevo_evento

def buscarEmprendimiento(db: Session, id: int):
    return db.query(ProyectoModelo).filter(ProyectoModelo.id_proyecto == id).first()

def obtenerEmprendimientos(db: Session):
    return db.query(ProyectoModelo).all()

def obtenerEmprendimientosPorEstado(db: Session, estado: str):
    return db.query(ProyectoModelo).filter(ProyectoModelo.estado == estado).all()

def eliminarEmprendimiento(db: Session, id: int):
    emprendimiento = buscarEmprendimiento(db, id)
    if not emprendimiento:
        raise HTTPException(status_code=404, detail="No se encontró el emprendimiento")

    db.delete(emprendimiento)
    db.commit()
    return {"detail": "Emprendimiento eliminado"}

def actualizarEmprendimiento(db: Session, emprendimiento: any):
    existente = buscarEmprendimiento(db, emprendimiento.id_proyecto)
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró el emprendimiento")
    
    if(existente.id_tipodocumento is None):
        raise HTTPException(status_code=400, detail="El emprendimiento debe estar asociado a un tipo de documento")
    
    auto_mapear(existente, emprendimiento, excluir=["id_usuario"])

    db.commit()
    db.refresh(existente)
    return existente