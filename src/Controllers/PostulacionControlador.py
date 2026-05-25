from sqlalchemy.orm import Session
from Schemas.PostulacionSchema import PostulacionCrearSchema, PostulacionActualizarSchema
from Services.PostulacionServicio import (ObtenerPostulacionesPorConvocatoria, ObtenerPostulacionesPorProyecto, BuscarPostulacion, CrearPostulacion, ActualizarPostulacion, CambiarEstadoPostulacion, EliminarPostulacion)

def obtener_postulaciones_por_convocatoria_controlador(db: Session, id_convocatoria: int):
    return ObtenerPostulacionesPorConvocatoria(db, id_convocatoria)

def obtener_postulaciones_por_proyecto_controlador(db: Session, id_proyecto: int):
    return ObtenerPostulacionesPorProyecto(db, id_proyecto)

def buscar_postulacion_controlador(db: Session, id_postulacion: int):
    return BuscarPostulacion(db, id_postulacion)

def crear_postulacion_controlador(db: Session, id_convocatoria: int, datos: PostulacionCrearSchema):
    return CrearPostulacion(db, id_convocatoria, datos)

def actualizar_postulacion_controlador(db: Session, id_postulacion: int, datos: PostulacionActualizarSchema):
    return ActualizarPostulacion(db, id_postulacion, datos)

def cambiar_estado_postulacion_controlador(db: Session, id_postulacion: int, nuevo_estado: str):
    return CambiarEstadoPostulacion(db, id_postulacion, nuevo_estado)

def eliminar_postulacion_controlador(db: Session, id_postulacion: int):
    return EliminarPostulacion(db, id_postulacion)