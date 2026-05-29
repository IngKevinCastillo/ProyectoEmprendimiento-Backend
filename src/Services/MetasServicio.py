from fastapi import HTTPException
from sqlalchemy import Date, extract
from sqlalchemy.orm import Session
from Models.MetasModelo import MetasModelo
from Schemas.MetasSchema import MetasActualizarSchema, MetasCrearSchema
from Utils.Mapeadorutilidades import auto_mapear

def buscarMeta(db: Session, id_meta: str):
    return db.query(MetasModelo).filter(MetasModelo.id_meta == int(id_meta)).first()

def obtenerMetas(db: Session):
    return db.query(MetasModelo).all()

def obtenerMetasPorAnio(db: Session, anio: str):
    return db.query(MetasModelo).filter(extract("year", MetasModelo.anio) == int(anio)).all()

def obtenerMetasPorEstado(db: Session, estado: str):
    return db.query(MetasModelo).filter(MetasModelo.id_estado == int(estado)).all()

def crearMeta(db: Session, meta: MetasCrearSchema):
    nueva_meta = MetasModelo()
    auto_mapear(nueva_meta, meta, excluir=["id_meta"])
    
    db.add(nueva_meta)
    db.commit()
    db.refresh(nueva_meta)
    return nueva_meta

def actualizarMeta(db: Session, id_meta: int, datos_actualizados: MetasActualizarSchema):
    existente = buscarMeta(db, id_meta)
    
    if not existente:
        raise HTTPException(status_code=404, detail="Meta no encontrada")
    
    datos_a_actualizar = datos_actualizados.model_dump(exclude_unset=True)

    for nombre_campo, valor_campo in datos_a_actualizar.items():
        setattr(existente, nombre_campo, valor_campo)
    
    db.commit()
    db.refresh(existente)
    return existente

def eliminarMeta(db: Session, id_meta: int):
    meta = buscarMeta(db, id_meta)
    
    if not meta:
        raise HTTPException(status_code=404, detail="Meta no encontrada")
    
    db.delete(meta)
    db.commit()
    return {"detail": "Meta eliminada"}

