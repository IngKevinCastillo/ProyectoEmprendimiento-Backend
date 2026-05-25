from sqlalchemy.orm import Session
from Schemas.EvaluacionSchema import EvaluacionCrearSchema
from Services.EvaluacionServicio import (BuscarEvaluacion, BuscarEvaluacionPorAsignacion, CrearEvaluacion, ActualizarComentario, CompletarEvaluacion)

def buscar_evaluacion_controlador(db: Session, id_evaluacion: int):
    return BuscarEvaluacion(db, id_evaluacion)

def buscar_evaluacion_por_asignacion_controlador(db: Session, id_asignacion: int):
    return BuscarEvaluacionPorAsignacion(db, id_asignacion)

def crear_evaluacion_controlador(db: Session, id_asignacion: int, datos: EvaluacionCrearSchema):
    return CrearEvaluacion(db, id_asignacion, datos)

def actualizar_comentario_controlador(db: Session, id_evaluacion: int, datos: EvaluacionCrearSchema):
    return ActualizarComentario(db, id_evaluacion, datos)

def completar_evaluacion_controlador(db: Session, id_evaluacion: int):
    return CompletarEvaluacion(db, id_evaluacion)