from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.FacultadModelo import FacultadModelo
from Utils.Mapeadorutilidades import auto_mapear
from Models.ProgramaModelo import ProgramaModelo

def BuscarFacultad(db: Session, id: str):
    return db.query(FacultadModelo).filter(FacultadModelo.id_facultad == int(id)).first()

def BuscarFacultadPorNombre(db: Session, nombre: str):
    return db.query(FacultadModelo).filter(FacultadModelo.nombre == nombre).first()

def ObtenerFacultades(db: Session):
    return db.query(FacultadModelo).all()

def BuscarProgramasPorFacultad(db: Session, id_facultad: str):
    return db.query(ProgramaModelo).filter(ProgramaModelo.id_facultad == int(id_facultad)).all()