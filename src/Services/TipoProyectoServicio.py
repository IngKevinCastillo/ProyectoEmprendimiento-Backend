from sqlalchemy.orm import Session
from Models.TipoProyectoModelo import TipoProyectoModelo

def buscar_tipo_proyecto(db: Session, id: int):
    return db.query(TipoProyectoModelo).filter(TipoProyectoModelo.id == id).first()

def buscar_tipo_proyecto_nombre(db: Session, nombre: str):
    return db.query(TipoProyectoModelo).filter(TipoProyectoModelo.nombre == nombre).first()

def obtener_tipos_proyectos(db: Session):
    return db.query(TipoProyectoModelo).all()