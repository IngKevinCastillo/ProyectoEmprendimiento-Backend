from sqlalchemy.orm import Session
from Models.SedeModelo import SedeModelo
from Utils.Mapeadorutilidades import auto_mapear

def obtener_sede_servicio(db: Session, id_sede: str):
    return db.query(SedeModelo).filter(SedeModelo.id_sede == int(id_sede)).first()

def obtener_sedes_servicio(db: Session):
    return db.query(SedeModelo).all()

def obtener_sede_por_nombre_servicio(db: Session, nombre: str):
    return db.query(SedeModelo).filter(SedeModelo.nombre == nombre).first()
