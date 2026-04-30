from sqlalchemy.orm import Session
from fastapi import HTTPException
from Schemas.ProyectoSchema import ProyectoCrearSchema
from Models.ProyectoModelo import ProyectoModelo
from Models.UsuarioProyectoModelo import UsuarioProyectoModelo

from Utils.Mapeadorutilidades import auto_mapear


def buscarEmprendimiento(db: Session, id: int):
    return db.query(ProyectoModelo).filter(ProyectoModelo.id_proyecto == id).first()

def buscarEmprendimientoPorNombre(db: Session, nombre: str):
    return db.query(ProyectoModelo).filter(ProyectoModelo.nombre_proyecto == nombre).first()

def obtenerEmprendimientos(db: Session):
    return db.query(ProyectoModelo).all()

def obtenerEmprendimientosPorEstado(db: Session, estado: str):
    return db.query(ProyectoModelo).filter(ProyectoModelo.estado == estado).all()

def crearEmprendimiento(db: Session, emprendimiento: ProyectoCrearSchema):
    existente = buscarEmprendimientoPorNombre(db, emprendimiento.nombre_proyecto)

    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un proyecto con ese nombre")

    nuevo_emprendimiento = ProyectoModelo(
        nombre_proyecto=emprendimiento.nombre_proyecto,
        descripcion=emprendimiento.descripcion,
        estado=emprendimiento.estado,
    )
    db.add(nuevo_emprendimiento)
    db.commit()
    db.refresh(nuevo_emprendimiento)
    return nuevo_emprendimiento

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

    auto_mapear(existente, emprendimiento, excluir=["id_proyecto"])

    db.commit()
    db.refresh(existente)
    return existente