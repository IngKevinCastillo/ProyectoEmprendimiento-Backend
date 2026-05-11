from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.EstadosModelo import EstadosModelo

def BuscarEstados(db: Session, id_estado: str):
    return db.query(EstadosModelo).filter(EstadosModelo.id_estado == int(id_estado)).first()

def BuscarEstadosPorNombre(db: Session, nombre: str):
    return db.query(EstadosModelo).filter(EstadosModelo.nombre == nombre).first()

def ObtenerEstados(db: Session):
    return db.query(EstadosModelo).all()