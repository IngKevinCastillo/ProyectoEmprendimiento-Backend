from sqlalchemy.orm import Session
from fastapi import HTTPException
from Utils.Mapeadorutilidades import auto_mapear
from Models.AlianzaModelo import AlianzaModelo
from Schemas.AlianzaSchema import AlianzaCrearSchema, AlianzaActualizarSchema

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
        descripcion=alianza.descripcion,
        sitio_web_url=alianza.sitio_web_url,
        id_tipo_entidad=alianza.id_tipo_entidad,
        orden=alianza.orden,
        activo=alianza.activo,
        representante=alianza.representante,
        correo_contacto=alianza.correo_contacto,
        telefono_contacto=alianza.telefono_contacto,
        fecha_inicio=alianza.fecha_inicio,
        fecha_fin=alianza.fecha_fin
    )
    db.add(nueva_alianza)
    db.commit()
    db.refresh(nueva_alianza)
    return nueva_alianza

def listar_alianzas(db: Session):
    return db.query(AlianzaModelo).all()

def actualizar_alianza(db: Session, id_alianza: str, alianza_actualizada: AlianzaActualizarSchema):
    existente = buscar_alianza(db, int(id_alianza))
    if not existente:
        raise HTTPException(status_code=404, detail="Alianza no encontrada")
    
    auto_mapear(existente, alianza_actualizada, exclude={"id_alianza"})
    db.commit()
    db.refresh(existente)
    return existente

