from sqlalchemy.orm import Session
from fastapi import HTTPException
from decimal import Decimal
from datetime import datetime
from Models.ProgramaModelo import ProgramaModelo
from Schemas.Programaschema import ProgramaCrearSchema

def BuscarPrograma(db: Session, id: int):
    return db.query(ProgramaModelo).filter(ProgramaModelo.id_programa == id).first()

def BuscarProgramaPorNombre(db: Session, nombre: str):
    return db.query(ProgramaModelo).filter(ProgramaModelo.nombre == nombre).first()

def ObtenerProgramas(db: Session):
    return db.query(ProgramaModelo).all()

def CrearPrograma(db: Session, programa: ProgramaCrearSchema):
    existente = BuscarProgramaPorNombre(db, programa.nombre)
    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un programa con ese nombre")
    
    if(programa.id_facultad is None):
        raise HTTPException(status_code=400, detail="El programa debe estar asociado a una facultad")

    nuevo_programa = ProgramaModelo(
        nombre=programa.nombre,
        nivel=programa.nivel,
        id_facultad=programa.id_facultad,
        estado=programa.estado
    )
    db.add(nuevo_programa)
    db.commit()
    db.refresh(nuevo_programa)
    return nuevo_programa

def EliminarPrograma(db: Session, id: int):
    programa = BuscarPrograma(db, id)
    if not programa:
        raise HTTPException(status_code=404, detail="No se encontró el programa")
    
    db.delete(programa)
    db.commit()
    return {"detail": "Programa eliminado"}

def ActualizarPrograma(db: Session, programaAActualizar: any):
    programa = BuscarPrograma(db, programaAActualizar.id_programa)
    if not programa:
        raise HTTPException(status_code=404, detail="No se encontró el programa")
    
    if(programa.id_facultad is None):
        raise HTTPException(status_code=400, detail="El programa debe estar asociado a una facultad")
    
    programa.nombre = programaAActualizar.nombre
    programa.estado = programaAActualizar.estado
    programa.nivel = programaAActualizar.nivel
    programa.id_facultad = programaAActualizar.id_facultad
    
    db.commit()
    db.refresh(programa)
    return programa