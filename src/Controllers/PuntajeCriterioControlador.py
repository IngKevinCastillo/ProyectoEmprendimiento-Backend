from sqlalchemy.orm import Session
from Schemas.PuntajeCriterioSchema import PuntajeCriterioCrearSchema, PuntajeCriterioActualizarSchema
from Services.PuntajeCriterioServicio import (ObtenerPuntajesPorEvaluacion, BuscarPuntaje, CrearPuntaje, ActualizarPuntaje, EliminarPuntaje)

def obtener_puntajes_por_evaluacion_controlador(db: Session, id_evaluacion: int):
    return ObtenerPuntajesPorEvaluacion(db, id_evaluacion)

def buscar_puntaje_controlador(db: Session, id_puntaje: int):
    return BuscarPuntaje(db, id_puntaje)

def crear_puntaje_controlador(db: Session, id_evaluacion: int, datos: PuntajeCriterioCrearSchema):
    return CrearPuntaje(db, id_evaluacion, datos)

def actualizar_puntaje_controlador(db: Session, id_puntaje: int, datos: PuntajeCriterioActualizarSchema):
    return ActualizarPuntaje(db, id_puntaje, datos)

def eliminar_puntaje_controlador(db: Session, id_puntaje: int):
    return EliminarPuntaje(db, id_puntaje)