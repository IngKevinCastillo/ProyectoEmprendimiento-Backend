
#from Utils.Mapeadorutilidades import auto_mapear
from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.AlianzaModelo import AlianzaModelo
from Schemas.AlianzaSchema import (AlianzaCrearSchema, AlianzaActualizarSchema)

def buscar_alianza(db: Session, id_alianza: int):
    return db.query(AlianzaModelo).filter(AlianzaModelo.id_alianza == id_alianza).first()

def buscar_alianza_por_nombre(db: Session, nombre_entidad: str):
    return db.query(AlianzaModelo).filter(AlianzaModelo.nombre_entidad == nombre_entidad).first()

def crear_alianza(db: Session, alianza: AlianzaCrearSchema):
    existente = buscar_alianza_por_nombre(db, alianza.nombre_entidad)
    if existente:
        raise HTTPException(status_code=400, detail="Ya existe una alianza con ese nombre")
    nueva_alianza = AlianzaModelo(
        nombre_entidad=alianza.nombre_entidad,
        sitio_web_url=str(alianza.sitio_web_url),
        id_tipo_entidad=alianza.id_tipo_entidad,
        representante_entidad=alianza.representante_entidad,
        correo_contacto=alianza.correo_contacto,
        telefono_contacto=alianza.telefono_contacto,
        fecha_inicio_alianza=alianza.fecha_inicio_alianza,
        fecha_fin_alianza=alianza.fecha_fin_alianza,
    )
    db.add(nueva_alianza)
    db.commit()
    db.refresh(nueva_alianza)
    return nueva_alianza

def listar_alianzas(db: Session):
    return db.query(AlianzaModelo).filter(AlianzaModelo.activo.is_(True)).all()

def actualizar_alianza(db: Session, id_alianza: int, alianza_actualizada: AlianzaActualizarSchema):
    existente = buscar_alianza(db, id_alianza)
    if not existente:
        raise HTTPException(status_code=404, detail="Alianza no encontrada")
    datos_actualizados = alianza_actualizada.dict(exclude_unset=True)
    datos_actualizados.pop("id_alianza", None)
    for campo, valor in datos_actualizados.items():
        setattr(existente, campo, valor)
    db.commit()
    db.refresh(existente)
    return existente

def desactivar_alianza(db: Session, id_alianza: int):
    alianza = buscar_alianza(db, id_alianza)
    if not alianza:
        raise HTTPException(status_code=404, detail="Alianza no encontrada")
    alianza.activo = False
    db.commit()
    db.refresh(alianza)
    return alianza

def activar_alianza(db: Session, id_alianza: int):
    alianza = buscar_alianza(db, id_alianza)
    if not alianza:
        raise HTTPException(status_code=404, detail="Alianza no encontrada")
    alianza.activo = True
    db.commit()
    db.refresh(alianza)
    return alianza
