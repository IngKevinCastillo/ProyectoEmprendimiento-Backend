from sqlalchemy.orm import Session
from Services.MunicipioServicio import buscar_municipio, buscar_municipio_nombre, listar_municipios

def buscar_municipio_controlador(db: Session, id_municipio: int):
    return buscar_municipio(db, id_municipio)

def buscar_municipio_nombre_controlador(db: Session, nombre: str):
    return buscar_municipio_nombre(db, nombre)

def listar_municipios_controlador(db: Session):
    return listar_municipios(db)