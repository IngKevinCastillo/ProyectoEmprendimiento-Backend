from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from Schemas.MesasSchema import MesasBaseSchema
from Models.MesasModelo import MesasModelo
from sqlalchemy import func

def buscar_mesa(db: Session, id: int):
    return db.query(MesasModelo).filter(MesasModelo.id == id).first()

def listar_mesas(db: Session):
    return db.query(MesasModelo).all()

def buscar_mesa_por_tutor(db: Session, documento: str):
    return db.query(MesasModelo).filter(MesasModelo.cedula_tutor == documento).first()

def buscar_mesa_por_docente(db: Session, documento: str):
    return db.query(MesasModelo).filter(MesasModelo.cedulas_docentes.any(documento)).first()

def buscar_mesa_por_nombre(db: Session, nombre: str):
    return db.query(MesasModelo).filter(MesasModelo.nombre == nombre).first()