from sqlalchemy.orm import Session
from Models.SedeModelo import SedeModelo
from Schemas.SedeSchemas import SedeCrearSchema, SedeActualizarSchema
from fastapi import HTTPException
from Utils.Mapeadorutilidades import auto_mapear

def crear_sede_servicio(db: Session, sede: SedeCrearSchema):
    existente = obtener_sede_por_nombre_servicio(db, sede.nombre)
    if existente:
        raise HTTPException(status_code=400, detail="Ya existe una sede con ese nombre")
    
    nueva_sede = SedeModelo(
        nombre=sede.nombre,
        ciudad=sede.ciudad
    )
    
    db.add(nueva_sede)
    db.commit()
    db.refresh(nueva_sede)
    return nueva_sede

def obtener_sede_servicio(db: Session, id_sede: str):
    return db.query(SedeModelo).filter(SedeModelo.id_sede == int(id_sede)).first()

def obtener_sedes_servicio(db: Session):
    return db.query(SedeModelo).all()

def obtener_sede_por_nombre_servicio(db: Session, nombre: str):
    return db.query(SedeModelo).filter(SedeModelo.nombre == nombre).first()

def actualizar_sede_servicio(db: Session, id_sede: str, sede: SedeActualizarSchema):
    existente = obtener_sede_servicio(db, id_sede)
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró la sede")
    
    auto_mapear(existente, sede, excluir=["id_sede"])
    
    db.commit()
    db.refresh(existente)
    return existente

def eliminar_sede_servicio(db: Session, id_sede: str):
    existente = obtener_sede_servicio(db, id_sede)
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró la sede")
    
    db.delete(existente)
    db.commit()
    return {"detail": "Sede eliminada"}
    