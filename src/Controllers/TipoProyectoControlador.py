from sqlalchemy.orm import Session
from Services.TipoProyectoServicio import buscar_tipo_proyecto, buscar_tipo_proyecto_nombre, obtener_tipos_proyectos

def listar_tipos_proyectos_controlador(db: Session):
    return obtener_tipos_proyectos(db)

def buscar_tipo_proyecto_controlador(db: Session, id: int):
    return buscar_tipo_proyecto(db, id)

def buscar_tipo_proyecto_por_nombre_controlador(db: Session, nombre: str):
    return buscar_tipo_proyecto_nombre(db, nombre)