from sqlalchemy.orm import Session
from Schemas.EstadosSchema import EstadosCrearSchema, EstadosRespuestaSchema
from Services.EstadosServicio import BuscarEstados, BuscarEstadosPorNombre, ObtenerEstados

def obtener_estados_controlador(db: Session):
    return ObtenerEstados(db)

def buscar_estados_controlador(db: Session, id_estado: str):
    return BuscarEstados(db, id_estado)

def obtener_estados_por_nombre_controlador(db: Session, nombre: str):
    return BuscarEstadosPorNombre(db, nombre)