from sqlalchemy.orm import Session
from Services.CategoriaServicio import buscar_categoria, buscar_categoria_nombre, listar_categorias

def buscar_categoria_controlador(db: Session, id_categoria: int):
    return buscar_categoria(db, id_categoria)

def buscar_categoria_nombre_controlador(db: Session, nombre_categoria: str):
    return buscar_categoria_nombre(db, nombre_categoria)

def listar_categorias_controlador(db: Session):
    return listar_categorias(db)