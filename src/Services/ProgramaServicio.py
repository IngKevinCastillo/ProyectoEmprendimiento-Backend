from sqlalchemy.orm import Session
from fastapi import HTTPException
from decimal import Decimal
from datetime import datetime
from Models.ProgramaModelo import ProgramaModelo
from Schemas.Programaschema import ProgramaCrearSchema
from Utils.Mapeadorutilidades import auto_mapear
from Services.FacultadServicio import BuscarFacultad

def BuscarPrograma(db: Session, id: str):
    return db.query(ProgramaModelo).filter(ProgramaModelo.id_programa == int(id)).first()

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
    
    if not BuscarFacultad(db, programa.id_facultad):
        raise HTTPException(status_code=400, detail="La facultad especificada no existe")

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

def EliminarPrograma(db: Session, id: str):
    existente = BuscarPrograma(db, int(id))
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró el programa")
    
    db.delete(existente)
    db.commit()
    return {"detail": "Programa eliminado"}

def ActualizarPrograma(db: Session, programa: any, id_programa: str):
    existente = BuscarPrograma(db, int(id_programa))
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró el programa")
    
    if(existente.id_facultad is None):
        raise HTTPException(status_code=400, detail="El programa debe estar asociado a una facultad")
    
    auto_mapear(existente, programa, excluir=["id_programa"])
    
    db.commit()
    db.refresh(existente)
    return existente