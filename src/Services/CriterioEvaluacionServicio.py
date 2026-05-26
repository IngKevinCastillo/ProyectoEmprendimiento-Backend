from sqlalchemy.orm import Session
from Models.CriterioEvaluacionModelo import CriterioEvaluacionModelo

def ObtenerCriterios(db: Session):
    return db.query(CriterioEvaluacionModelo).all()

def BuscarCriterio(db: Session, id_criterio: int):
    return db.query(CriterioEvaluacionModelo).filter(
        CriterioEvaluacionModelo.id_criterio == id_criterio
    ).first()