from sqlalchemy.orm import Session
from Schemas.DepartamentoSchema import DepartamentoRespuestaSchema
from Models.DepartamentoModelo import DepartamentoModelo

def buscar_departamento(db: Session, id_departamento: int):
    return db.query(DepartamentoModelo).filter(DepartamentoModelo.id_departamento == id_departamento).first()

def listar_departamentos(db: Session):
    return db.query(DepartamentoModelo).all()

def buscar_departamento_nombre(db: Session, nombre: str):
    return db.query(DepartamentoModelo).filter(DepartamentoModelo.nombre == nombre).first()