from sqlalchemy.orm import Session
from Services.MesasServicio import buscar_mesa, buscar_mesa_por_docente, buscar_mesa_por_nombre, buscar_mesa_por_tutor, listar_mesas

def buscar_mesa_controlador(db: Session, id: int):
    return buscar_mesa(db, id)

def listar_mesas_controlador(db: Session):
    return listar_mesas(db)

def buscar_mesa_por_tutor_controlador(db: Session, documento: str):
    return buscar_mesa_por_tutor(db, documento)

def buscar_mesa_por_docente_controlador(db: Session, documento: str):
    return buscar_mesa_por_docente(db, documento)

def buscar_mesa_por_nombre_controlador(db: Session, nombre: str):
    return buscar_mesa_por_nombre(db, nombre)