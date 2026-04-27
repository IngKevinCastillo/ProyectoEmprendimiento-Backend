from sqlalchemy.orm import Session
from Schemas.Tipodocumentoschema import TipoDocumentoCrearSchema, TipoDocumentoRespuestaSchema, TipoDocumentoActualizarSchema
from Services.TipoDocumentoServicio import CrearTipoDocumento, BuscarTipoDocumento, EliminarTipoDocumento, ActualizarTipoDocumento, BuscarTipoDocumentoPorNombre, ObtenerTiposDocumento

def crear_tipo_documento_controlador(db: Session, datos: TipoDocumentoCrearSchema):
    return CrearTipoDocumento(db, datos)

def obtener_tipo_documento_controlador(db: Session, id_tipo_documento: str):
    return BuscarTipoDocumento(db, id_tipo_documento)

def obtener_tipo_documento_nombre_controlador(db: Session, nombre: str):
    return BuscarTipoDocumentoPorNombre(db, nombre)

def listar_tipos_documento_controlador(db: Session):
    return ObtenerTiposDocumento(db)

def actualizar_tipo_documento_controlador(db: Session, datos: TipoDocumentoActualizarSchema, id_tipo_documento: str):
    return ActualizarTipoDocumento(db, datos, id_tipo_documento)

def eliminar_tipo_documento_controlador(db: Session, id_tipo_documento: str):
    return EliminarTipoDocumento(db, id_tipo_documento)