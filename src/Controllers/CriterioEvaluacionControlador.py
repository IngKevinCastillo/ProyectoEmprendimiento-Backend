from sqlalchemy.orm import Session
from Services.CriterioEvaluacionServicio import ObtenerCriterios, BuscarCriterio

def obtener_criterios_controlador(db: Session):
    return ObtenerCriterios(db)

def buscar_criterio_controlador(db: Session, id_criterio: int):
    return BuscarCriterio(db, id_criterio)