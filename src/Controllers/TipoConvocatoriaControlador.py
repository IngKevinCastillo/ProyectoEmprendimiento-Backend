from sqlalchemy.orm import Session
from Schemas.TipoConvocatoriaSchema import TipoConvocatoriaCrearSchema, TipoConvocatoriaActualizarSchema
from Services.TipoConvocatoriaServicio import (ObtenerTiposConvocatoria, BuscarTipoConvocatoria, CrearTipoConvocatoria, ActualizarTipoConvocatoria, EliminarTipoConvocatoria)

def obtener_tipos_convocatoria_controlador(db: Session):
    return ObtenerTiposConvocatoria(db)

def buscar_tipo_convocatoria_controlador(db: Session, id_tipo_convocatoria: int):
    return BuscarTipoConvocatoria(db, id_tipo_convocatoria)

def crear_tipo_convocatoria_controlador(db: Session, datos: TipoConvocatoriaCrearSchema):
    return CrearTipoConvocatoria(db, datos)

def actualizar_tipo_convocatoria_controlador(db: Session, id_tipo_convocatoria: int, datos: TipoConvocatoriaActualizarSchema):
    return ActualizarTipoConvocatoria(db, id_tipo_convocatoria, datos)

def eliminar_tipo_convocatoria_controlador(db: Session, id_tipo_convocatoria: int):
    return EliminarTipoConvocatoria(db, id_tipo_convocatoria)