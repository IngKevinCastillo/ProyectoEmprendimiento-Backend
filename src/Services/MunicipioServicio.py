from sqlalchemy.orm import Session
from Models.MunicipioModelo import MunicipioModelo

def buscar_municipio(db: Session, id_municipio: int):
    return db.query(MunicipioModelo).filter(MunicipioModelo.id_municipio == id_municipio).first()

def listar_municipios(db: Session):
    return db.query(MunicipioModelo).all()

def buscar_municipio_nombre(db: Session, nombre: str):
    return db.query(MunicipioModelo).filter(MunicipioModelo.nombre == nombre).first()