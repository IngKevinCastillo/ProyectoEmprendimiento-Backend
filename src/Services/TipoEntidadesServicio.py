from sqlalchemy.orm import Session
from fastapi import HTTPException
from Utils.Mapeadorutilidades import auto_mapear
from Models.TipoEntidadModelo import TipoEntidadModelo
from Schemas.TipoEntidadSchema import TipoEntidadCrearSchema, TipoEntidadActualizarSchema

def buscar_tipo_entidad(db: Session, id_tipo_entidad: int):
    return db.query(TipoEntidadModelo).filter(TipoEntidadModelo.id_tipo_entidad == id_tipo_entidad).first()

def buscar_tipo_entidad_por_nombre(db: Session, nombre_tipo_entidad: str):
    return db.query(TipoEntidadModelo).filter(TipoEntidadModelo.nombre_tipo_entidad == nombre_tipo_entidad).first()

def crear_tipo_entidad(db: Session, tipo_entidad: TipoEntidadCrearSchema):
    existente = buscar_tipo_entidad_por_nombre(db, tipo_entidad.nombre_tipo_entidad)
    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un tipo de entidad con ese nombre")
    nuevo_tipo_entidad = TipoEntidadModelo(
        nombre_tipo_entidad=tipo_entidad.nombre_tipo_entidad
    )
    db.add(nuevo_tipo_entidad)
    db.commit()
    db.refresh(nuevo_tipo_entidad)
    return nuevo_tipo_entidad

def listar_tipo_entidades(db: Session):
    return db.query(TipoEntidadModelo).all()

def actualizar_tipo_entidad(db: Session, id_tipo_entidad: str, tipo_entidad_actualizado: TipoEntidadActualizarSchema):
    existente = buscar_tipo_entidad(db, int(id_tipo_entidad))
    if not existente:
        raise HTTPException(status_code=404, detail="Tipo de entidad no encontrado")
    
    auto_mapear(existente, tipo_entidad_actualizado, exclude={"id_tipo_entidad"})
    db.commit()
    db.refresh(existente)
    return existente

