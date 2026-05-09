from sqlalchemy.orm import Session
from Models.CategoriaModelo import CategoriaModelo

def buscar_categoria(db: Session, id_categoria: int):
    return db.query(CategoriaModelo).filter(CategoriaModelo.id_categoria == id_categoria).first()

def buscar_categoria_nombre(db: Session, nombre_categoria: str):
    return db.query(CategoriaModelo).filter(CategoriaModelo.nombre_categoria == nombre_categoria).first()

def listar_categorias(db: Session):
    return db.query(CategoriaModelo).all()