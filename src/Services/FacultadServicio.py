from sqlalchemy.orm import Session
from fastapi import HTTPException
from decimal import Decimal
from datetime import datetime
from Models.FacultadModelo import FacultadModelo

def BuscarFacultad(db: Session, id: int):
    return db.query(FacultadModelo).filter(FacultadModelo.id_facultad == id).first()

def BuscarFacultadPorNombre(db: Session, nombre: str):
    return db.query(FacultadModelo).filter(FacultadModelo.nombre == nombre).first()

def ObtenerFacultades(db: Session):
    return db.query(FacultadModelo).all()

def CrearFacultad(db: Session, facultad: any):
    existente = BuscarFacultadPorNombre(db, facultad.nombre)
    if existente:
        raise HTTPException(status_code=400, detail="Ya existe una facultad con ese nombre")

    nueva_facultad = FacultadModelo(
        id_facultad=facultad.id_facultad,
        nombre=facultad.nombre,
        descripcion=facultad.descripcion,
        estado=facultad.estado
    )
    db.add(nueva_facultad)
    db.commit()
    db.refresh(nueva_facultad)
    return nueva_facultad

def EliminarFacultad(db: Session, id: int):
    facultad = BuscarFacultad(db, id)
    if not facultad:
        raise HTTPException(status_code=404, detail="No se encontró la facultad")
    
    db.delete(facultad)
    db.commit()
    return {"detail": "Facultad eliminada"}

def ActualizarFacultad(db: Session, facultadAActualizar: any):
    facultad = BuscarFacultad(db, facultadAActualizar.id_facultad)
    if not facultad:
        raise HTTPException(status_code=404, detail="No se encontró la facultad")
    
    facultad.nombre = facultadAActualizar.nombre
    facultad.descripcion = facultadAActualizar.descripcion
    facultad.estado = facultadAActualizar.estado

    db.commit()
    db.refresh(facultad)
    return facultad