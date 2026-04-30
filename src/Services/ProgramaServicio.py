from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.ProgramaModelo import ProgramaModelo

def BuscarPrograma(db: Session, id: str):
    return db.query(ProgramaModelo).filter(ProgramaModelo.id_programa == int(id)).first()

def BuscarProgramaPorNombre(db: Session, nombre: str):
    return db.query(ProgramaModelo).filter(ProgramaModelo.nombre == nombre).first()

def ObtenerProgramas(db: Session):
    return db.query(ProgramaModelo).all()