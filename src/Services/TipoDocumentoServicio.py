from sqlalchemy.orm import Session
from fastapi import HTTPException
from decimal import Decimal
from datetime import datetime
from Models.TipoDocumentoModelo import TipoDocumentoModelo

def BuscarTipoDocumento(db: Session, id: int):
    return db.query(TipoDocumentoModelo).filter(TipoDocumentoModelo.id_tipo_documento == id).first()

def BuscarTipoDocumentoPorNombre(db: Session, nombre: str):
    return db.query(TipoDocumentoModelo).filter(TipoDocumentoModelo.nombre == nombre).first()

def ObtenerTiposDocumento(db: Session):
    return db.query(TipoDocumentoModelo).all()

def CrearTipoDocumento(db: Session, tipo_documento: any):
    existente = BuscarTipoDocumentoPorNombre(db, tipo_documento.nombre)
    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un tipo de documento con ese nombre")

    nuevo_tipo_documento = TipoDocumentoModelo(
        id_tipo_documento=tipo_documento.id_tipo_documento,
        nombre=tipo_documento.nombre,
        abreviatura=tipo_documento.abreviatura,
        estado=tipo_documento.estado
    )
    db.add(nuevo_tipo_documento)
    db.commit()
    db.refresh(nuevo_tipo_documento)
    return nuevo_tipo_documento

def EliminarTipoDocumento(db: Session, id: int):
    tipo_documento = BuscarTipoDocumento(db, id)
    if not tipo_documento:
        raise HTTPException(status_code=404, detail="No se encontró el tipo de documento")

    db.delete(tipo_documento)
    db.commit()
    return {"detail": "Tipo de documento eliminado"}

def ActualizarTipoDocumento(db: Session, tipo_documentoAActualizar: any):
    tipo_documento = BuscarTipoDocumento(db, tipo_documentoAActualizar.id_tipo_documento)
    if not tipo_documento:
        raise HTTPException(status_code=404, detail="No se encontró el tipo de documento")

    tipo_documento.nombre = tipo_documentoAActualizar.nombre
    tipo_documento.abreviatura = tipo_documentoAActualizar.abreviatura
    tipo_documento.estado = tipo_documentoAActualizar.estado

    db.commit()
    db.refresh(tipo_documento)
    return tipo_documento