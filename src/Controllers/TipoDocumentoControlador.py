from sqlalchemy.orm import Session
from Services.TipoDocumentoServicio import BuscarTipoDocumento, BuscarTipoDocumentoPorNombre, ObtenerTiposDocumento

def obtener_tipo_documento_controlador(db: Session, id_tipo_documento: str):
    return BuscarTipoDocumento(db, id_tipo_documento)

def obtener_tipo_documento_nombre_controlador(db: Session, nombre: str):
    return BuscarTipoDocumentoPorNombre(db, nombre)

def listar_tipos_documento_controlador(db: Session):
    return ObtenerTiposDocumento(db)