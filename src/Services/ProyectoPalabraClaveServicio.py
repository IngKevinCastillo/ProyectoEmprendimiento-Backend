from typing import Final
from sqlalchemy.orm import Session
from Schemas.ProyectoPalabraClaveSchema import ProyectoPalabraClaveCrearSchema, ProyectoPalabraClaveActualizarSchema
from Models.ProyectoPalabraClaveModelo import ProyectoPalabraClaveModelo
from fastapi import HTTPException, status
from Utils.Mapeadorutilidades import auto_mapear
from Models.ProyectoModelo import ProyectoModelo
from Core.CacheResolver import obtener_id_estado

ESTADO_ELIMINADO: Final = "Eliminado"

def crear_proyecto_palabra_clave(db: Session, proyecto_palabra_clave: ProyectoPalabraClaveCrearSchema):
    existentes = listar_proyecto_palabra_clave(db, proyecto_palabra_clave.id_proyecto)
    
    if len(existentes) > 5:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El proyecto especificado ya tiene palabras claves...debes actualizar las palabras ya existentes o eliminar alguna(s).")
    
    proyecto_palabra_clave_nuevo = ProyectoPalabraClaveModelo(
        id_proyecto = proyecto_palabra_clave.id_proyecto,
        id_palabra_clave = proyecto_palabra_clave.id_palabra_clave
    )
    
    db.add(proyecto_palabra_clave_nuevo)
    db.commit()
    db.refresh(proyecto_palabra_clave_nuevo)
    return proyecto_palabra_clave_nuevo

def buscar_proyecto_palabra_clave(db: Session, id_proyecto_palabra_clave: int):
    return db.query(ProyectoPalabraClaveModelo).join(
        ProyectoModelo, ProyectoPalabraClaveModelo.id_proyecto == ProyectoModelo.id_proyecto).filter(ProyectoPalabraClaveModelo.id_proyecto_palabra_clave == id_proyecto_palabra_clave, ProyectoModelo.id_estado != obtener_id_estado(db, ESTADO_ELIMINADO)).first()

def listar_proyecto_palabra_clave(db: Session, id_proyecto: int):
    return db.query(ProyectoPalabraClaveModelo).join(
        ProyectoModelo, ProyectoPalabraClaveModelo.id_proyecto == ProyectoModelo.id_proyecto).filter(ProyectoPalabraClaveModelo.id_proyecto == id_proyecto,ProyectoModelo.id_estado != obtener_id_estado(db, ESTADO_ELIMINADO)).all()

def actualizar_proyecto_palabra_clave(db: Session, id_proyecto_palabra_clave: int, proyecto_palabra_clave: ProyectoPalabraClaveActualizarSchema):
    existente = buscar_proyecto_palabra_clave(db, id_proyecto_palabra_clave)
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La palabra clave del proyecto especificada no existe.")
    
    auto_mapear(existente, proyecto_palabra_clave, excluir=["id_proyecto_palabra_clave"])
    
    db.commit()
    db.refresh(existente)
    return existente

def elimina_proyecto_palabra_clave(db: Session, id_proyecto_palabra_clave: int):
    existente = buscar_proyecto_palabra_clave(db, id_proyecto_palabra_clave)
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La palabra clave del proyecto especificada no existe.")
    
    db.delete(existente)
    db.commit()
    return {"detail": "Emprendimiento eliminado"}