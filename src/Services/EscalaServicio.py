from sqlalchemy.orm import Session
from Models.EscalaModelo import EscalaModelo

def buscar_escala(db: Session, id: int):
    return db.query(EscalaModelo).filter(EscalaModelo.id == id).first()

def buscar_escala_nombre(db: Session, nombre: str):
    return db.query(EscalaModelo).filter(EscalaModelo.nombre == nombre).first()

def obtener_escalas(db: Session):
    return db.query(EscalaModelo).all()