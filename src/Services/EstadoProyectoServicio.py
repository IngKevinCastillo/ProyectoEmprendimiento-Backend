from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.EstadoProyectoModelo import EstadoProyectoModelo

def BuscarEstadoProyecto(db: Session, id_estado_proyecto: str):
    return db.query(EstadoProyectoModelo).filter(EstadoProyectoModelo.id_estado_proyecto == int(id_estado_proyecto)).first()

def BuscarEstadoProyectoPorNombre(db: Session, nombre: str):
    return db.query(EstadoProyectoModelo).filter(EstadoProyectoModelo.nombre == nombre).first()

def ObtenerEstadosProyectos(db: Session):
    return db.query(EstadoProyectoModelo).all()