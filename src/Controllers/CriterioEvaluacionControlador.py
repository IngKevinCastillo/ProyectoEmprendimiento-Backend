from sqlalchemy.orm import Session
from Schemas.CriterioEvaluacionSchema import CriterioCrearSchema, CriterioActualizarSchema
from Services.CriterioEvaluacionServicio import (
    ObtenerCriteriosPorConvocatoria,
    BuscarCriterio,
    CrearCriterio,
    ActualizarCriterio,
    EliminarCriterio
)

def obtener_criterios_controlador(db: Session, id_convocatoria: int):
    return ObtenerCriteriosPorConvocatoria(db, id_convocatoria)

def buscar_criterio_controlador(db: Session, id_criterio: int):
    return BuscarCriterio(db, id_criterio)

def crear_criterio_controlador(db: Session, id_convocatoria: int, datos: CriterioCrearSchema):
    return CrearCriterio(db, id_convocatoria, datos)

def actualizar_criterio_controlador(db: Session, id_criterio: int, datos: CriterioActualizarSchema):
    return ActualizarCriterio(db, id_criterio, datos)

def eliminar_criterio_controlador(db: Session, id_criterio: int):
    return EliminarCriterio(db, id_criterio)