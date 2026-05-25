from sqlalchemy.orm import Session
from Schemas.ConvocatoriaSchema import ConvocatoriaCrearSchema, ConvocatoriaActualizarSchema
from Services.ConvocatoriaServicio import (ObtenerConvocatorias, ObtenerConvocatoriasPublicadas, BuscarConvocatoria, CrearConvocatoria, ActualizarConvocatoria, CambiarEstadoConvocatoria, EliminarConvocatoria)

def obtener_convocatorias_controlador(db: Session):
    return ObtenerConvocatorias(db)

def obtener_convocatorias_publicadas_controlador(db: Session):
    return ObtenerConvocatoriasPublicadas(db)

def buscar_convocatoria_controlador(db: Session, id_convocatoria: int):
    return BuscarConvocatoria(db, id_convocatoria)

def crear_convocatoria_controlador(db: Session, datos: ConvocatoriaCrearSchema, id_admin: int):
    return CrearConvocatoria(db, datos, id_admin)

def actualizar_convocatoria_controlador(db: Session, id_convocatoria: int, datos: ConvocatoriaActualizarSchema):
    return ActualizarConvocatoria(db, id_convocatoria, datos)

def cambiar_estado_convocatoria_controlador(db: Session, id_convocatoria: int, nuevo_estado: str):
    return CambiarEstadoConvocatoria(db, id_convocatoria, nuevo_estado)

def eliminar_convocatoria_controlador(db: Session, id_convocatoria: int):
    return EliminarConvocatoria(db, id_convocatoria)