from sqlalchemy.orm import Session
from Schemas.IndicadorSchema import IndicadorCrearSchema, IndicadorActualizarSchema
from Services.IndicadorServicio import crearIndicador, buscarIndicador, obtenerIndicadores, obtenerIndicadoresPorProyecto, eliminarIndicador, actualizarIndicador, buscarIndicadorPorNombre

def crear_indicador_controlador(db: Session, indicador: IndicadorCrearSchema):
    return crearIndicador(db, indicador)

def obtener_indicadores_controlador(db: Session):
    return obtenerIndicadores(db)

def obtener_indicadores_por_proyecto_controlador(db: Session, id_proyecto: str):
    return obtenerIndicadoresPorProyecto(db, id_proyecto)

def buscar_indicador_controlador(db: Session, id_indicador: str):
    return buscarIndicador(db, id_indicador)

def buscar_indicador_por_nombre_controlador(db: Session, nombre: str):
    return buscarIndicadorPorNombre(db, nombre)

def eliminar_indicador_controlador(db: Session, id_indicador: str):
    return eliminarIndicador(db, id_indicador)

def actualizar_indicador_controlador(db: Session, indicador: IndicadorActualizarSchema, id_indicador: str):
    return actualizarIndicador(db, indicador, id_indicador)