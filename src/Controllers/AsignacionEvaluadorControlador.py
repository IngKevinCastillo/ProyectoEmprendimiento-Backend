from sqlalchemy.orm import Session
from Schemas.AsignacionEvaluadorSchema import AsignacionCrearSchema
from Services.AsignacionEvaluadorServicio import (ObtenerAsignacionesPorPostulacion, ObtenerAsignacionesPorEvaluador, BuscarAsignacion, CrearAsignacion, EliminarAsignacion)

def obtener_asignaciones_por_postulacion_controlador(db: Session, id_postulacion: int):
    return ObtenerAsignacionesPorPostulacion(db, id_postulacion)

def obtener_asignaciones_por_evaluador_controlador(db: Session, id_evaluador: int):
    return ObtenerAsignacionesPorEvaluador(db, id_evaluador)

def buscar_asignacion_controlador(db: Session, id_asignacion: int):
    return BuscarAsignacion(db, id_asignacion)

def crear_asignacion_controlador(db: Session, id_postulacion: int, datos: AsignacionCrearSchema):
    return CrearAsignacion(db, id_postulacion, datos)

def eliminar_asignacion_controlador(db: Session, id_asignacion: int):
    return EliminarAsignacion(db, id_asignacion)