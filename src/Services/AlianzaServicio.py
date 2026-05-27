from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.AlianzaModelo import AlianzaModelo
from Models.EstadosModelo import EstadosModelo
from Schemas.AlianzaSchema import (AlianzaCrearSchema, AlianzaActualizarSchema)

def buscar_alianza(db: Session, id_alianza: int):
    return db.query(AlianzaModelo).filter(AlianzaModelo.id_alianza == id_alianza).first()

def buscar_alianza_por_nombre(db: Session, nombre_entidad: str):
    return db.query(AlianzaModelo).filter(AlianzaModelo.nombre_entidad == nombre_entidad).first()

def crear_alianza(db: Session, alianza: AlianzaCrearSchema):
    existente = buscar_alianza_por_nombre(db, alianza.nombre_entidad)
    if existente:
        raise HTTPException(status_code=400, detail="Ya existe una alianza con ese nombre")
    estado = db.query(EstadosModelo).filter(
        EstadosModelo.id_estado == alianza.id_estado).first()
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    nueva_alianza = AlianzaModelo(
        nombre_entidad=alianza.nombre_entidad,
        sitio_web_url=str(alianza.sitio_web_url),
        id_tipo_entidad=alianza.id_tipo_entidad,
        id_estado=alianza.id_estado,
        representante_entidad=alianza.representante_entidad,
        correo_contacto=alianza.correo_contacto,
        telefono_contacto=alianza.telefono_contacto,
        fecha_inicio_alianza=alianza.fecha_inicio_alianza,
        fecha_fin_alianza=alianza.fecha_fin_alianza,
        convenio_pdf_url=alianza.convenio_pdf_url,
    )
    db.add(nueva_alianza)
    db.commit()
    db.refresh(nueva_alianza)
    return nueva_alianza

def listar_alianzas(db: Session, id_estado: int | None = None):
    query = db.query(AlianzaModelo)
    if id_estado is not None:
        query = query.filter(AlianzaModelo.id_estado == id_estado)
    return query.all()

def actualizar_alianza(db: Session, id_alianza: int, alianza_actualizada: AlianzaActualizarSchema):
    existente = buscar_alianza(db, id_alianza)
    if not existente:
        raise HTTPException(status_code=404, detail="Alianza no encontrada")
    datos_actualizados = alianza_actualizada.dict(exclude_unset=True)
    datos_actualizados.pop("id_alianza", None)
    datos_actualizados.pop("fecha_registro_alianza", None)
    if "id_estado" in datos_actualizados:
        estado = db.query(EstadosModelo).filter(
            EstadosModelo.id_estado == datos_actualizados["id_estado"]).first()
        if not estado:
            raise HTTPException(status_code=404, detail="Estado no encontrado")
    for campo, valor in datos_actualizados.items():
        setattr(existente, campo, valor)
    db.commit()
    db.refresh(existente)
    return existente

def cambiar_estado_alianza(db: Session, id_alianza: int, id_estado: int):
    alianza = buscar_alianza(db, id_alianza)
    if not alianza:
        raise HTTPException(status_code=404, detail="Alianza no encontrada")
    estado = db.query(EstadosModelo).filter(EstadosModelo.id_estado == id_estado).first()
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    alianza.id_estado = id_estado
    db.commit()
    db.refresh(alianza)
    return alianza

def buscar_estado_por_nombre(db: Session, nombre: str):
    return db.query(EstadosModelo).filter(
        EstadosModelo.nombre == nombre
    ).first()
