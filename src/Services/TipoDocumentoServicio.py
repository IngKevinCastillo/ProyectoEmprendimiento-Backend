from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.TipoDocumentoModelo import TipoDocumentoModelo
def BuscarTipoDocumento(db: Session, id_tipo_documento: str):
    return db.query(TipoDocumentoModelo).filter(TipoDocumentoModelo.id_tipo_documento == int(id_tipo_documento)).first()

def BuscarTipoDocumentoPorNombre(db: Session, nombre: str):
    return db.query(TipoDocumentoModelo).filter(TipoDocumentoModelo.nombre == nombre).first()

def ObtenerTiposDocumento(db: Session):
    return db.query(TipoDocumentoModelo).all()