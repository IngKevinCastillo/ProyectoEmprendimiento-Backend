from sqlalchemy.orm import Session
from Services.DepartamentoServicio import buscar_departamento, buscar_departamento_nombre, listar_departamentos

def buscar_departamento_controlador(db: Session, id_departamento: int):
    return buscar_departamento(db, id_departamento)

def buscar_departamento_nombre_controlador(db: Session, nombre: str):
    return buscar_departamento_nombre(db, nombre)

def listar_departamentos_controlador(db: Session):
    return listar_departamentos(db)