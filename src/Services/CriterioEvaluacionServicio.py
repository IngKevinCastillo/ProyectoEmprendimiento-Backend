from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.CriterioEvaluacionModelo import CriterioEvaluacionModelo
from Models.ConvocatoriaModelo import ConvocatoriaModelo
from Schemas.CriterioEvaluacionSchema import CriterioCrearSchema, CriterioActualizarSchema

ID_ESTADO_CONVOCATORIA_PUBLICADA = 19

def _validar_convocatoria_editable(db: Session, id_convocatoria: int):
    convocatoria = db.query(ConvocatoriaModelo).filter(
        ConvocatoriaModelo.id_convocatoria == id_convocatoria
    ).first()
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatoria no encontrada")
    if convocatoria.id_estado != ID_ESTADO_CONVOCATORIA_PUBLICADA:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se pueden gestionar criterios de convocatorias publicadas"
        )
    return convocatoria

def ObtenerCriteriosPorConvocatoria(db: Session, id_convocatoria: int):
    return db.query(CriterioEvaluacionModelo).filter(
        CriterioEvaluacionModelo.id_convocatoria == id_convocatoria
    ).all()

def BuscarCriterio(db: Session, id_criterio: int):
    return db.query(CriterioEvaluacionModelo).filter(
        CriterioEvaluacionModelo.id_criterio == id_criterio
    ).first()

def CrearCriterio(db: Session, id_convocatoria: int, datos: CriterioCrearSchema):
    _validar_convocatoria_editable(db, id_convocatoria)
    nuevo = CriterioEvaluacionModelo(
        id_convocatoria=id_convocatoria,
        **datos.model_dump()
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def ActualizarCriterio(db: Session, id_criterio: int, datos: CriterioActualizarSchema):
    criterio = BuscarCriterio(db, id_criterio)
    if not criterio:
        return None
    _validar_convocatoria_editable(db, criterio.id_convocatoria)
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(criterio, campo, valor)
    db.commit()
    db.refresh(criterio)
    return criterio

def EliminarCriterio(db: Session, id_criterio: int):
    criterio = BuscarCriterio(db, id_criterio)
    if not criterio:
        return None
    _validar_convocatoria_editable(db, criterio.id_convocatoria)
    db.delete(criterio)
    db.commit()
    return True