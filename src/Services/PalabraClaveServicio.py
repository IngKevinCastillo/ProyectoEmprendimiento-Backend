from sqlalchemy.orm import Session
from Schemas.PalabraClaveSchema import PalabraClaveCrearSchema, PalabraClaveActualizarSchema
from Models.PalabraClaveModelo import PalabraClaveModelo
from fastapi import HTTPException, status
from Utils.Mapeadorutilidades import auto_mapear

def crear_palabra_clave(db: Session, palabra_clave: PalabraClaveCrearSchema):
    existente = buscar_palabra_clave_palabra(db, palabra_clave.palabra)
    
    if existente:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="La palabra clave especificada ya existe.")
    
    palabra_clave_nueva = PalabraClaveModelo(
        palabra=palabra_clave.palabra
    )
    
    db.add(palabra_clave_nueva)
    db.commit()
    db.refresh(palabra_clave_nueva)
    return palabra_clave_nueva

def buscar_palabra_clave(db: Session, id_palabra_clave: int):
    return db.query(PalabraClaveModelo).filter(PalabraClaveModelo.id_palabra_clave == id_palabra_clave).first()

def buscar_palabra_clave_palabra(db: Session, palabra: str):
    return db.query(PalabraClaveModelo).filter(PalabraClaveModelo.palabra == palabra).first()

def listar_palabras_clave(db: Session):
    return db.query(PalabraClaveModelo).all()

def actualizar_palabra_clave(db: Session, id_palabra_clave: int, palabra_clave: PalabraClaveActualizarSchema):
    existente = buscar_palabra_clave(db, id_palabra_clave)
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La palabra clave especificada no existe.")
    
    auto_mapear(existente, palabra_clave, excluir=["id_palabra_clave"])
    
    db.commit()
    db.refresh(existente)
    return existente