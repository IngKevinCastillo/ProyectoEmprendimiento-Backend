from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from decimal import Decimal
from Models.PuntajeCriterioModelo import PuntajeCriterioModelo
from Models.EvaluacionModelo import EvaluacionModelo
from Models.CriterioEvaluacionModelo import CriterioEvaluacionModelo
from Schemas.PuntajeCriterioSchema import PuntajeCriterioCrearSchema, PuntajeCriterioActualizarSchema

ID_ESTADO_COMPLETADA = 28

def _validar_evaluacion_editable(db: Session, id_evaluacion: int):
    evaluacion = db.query(EvaluacionModelo).filter(
        EvaluacionModelo.id_evaluacion == id_evaluacion
    ).first()
    if not evaluacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evaluación no encontrada")
    if evaluacion.id_estado == ID_ESTADO_COMPLETADA:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pueden modificar puntajes de una evaluación completada"
        )
    return evaluacion

def _recalcular_puntaje_total(db: Session, evaluacion: EvaluacionModelo):
    puntajes = db.query(PuntajeCriterioModelo).filter(
        PuntajeCriterioModelo.id_evaluacion == evaluacion.id_evaluacion
    ).all()
    total = Decimal("0.00")
    for p in puntajes:
        criterio = db.query(CriterioEvaluacionModelo).filter(
            CriterioEvaluacionModelo.id_criterio == p.id_criterio
        ).first()
        total += p.nota * criterio.porcentaje / Decimal("100")
    evaluacion.puntaje_total = round(total, 2)
    db.commit()

def ObtenerPuntajesPorEvaluacion(db: Session, id_evaluacion: int):
    return db.query(PuntajeCriterioModelo).filter(
        PuntajeCriterioModelo.id_evaluacion == id_evaluacion
    ).all()

def BuscarPuntaje(db: Session, id_puntaje: int):
    return db.query(PuntajeCriterioModelo).filter(
        PuntajeCriterioModelo.id_puntaje == id_puntaje
    ).first()

def CrearPuntaje(db: Session, id_evaluacion: int, datos: PuntajeCriterioCrearSchema):
    evaluacion = _validar_evaluacion_editable(db, id_evaluacion)

    criterio = db.query(CriterioEvaluacionModelo).filter(
        CriterioEvaluacionModelo.id_criterio == datos.id_criterio
    ).first()
    if not criterio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Criterio no encontrado")

    existe = db.query(PuntajeCriterioModelo).filter(
        PuntajeCriterioModelo.id_evaluacion == id_evaluacion,
        PuntajeCriterioModelo.id_criterio == datos.id_criterio
    ).first()
    if existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este criterio ya tiene una nota registrada en esta evaluación"
        )

    nuevo = PuntajeCriterioModelo(
        id_evaluacion=id_evaluacion,
        id_criterio=datos.id_criterio,
        nota=datos.nota,
    )
    db.add(nuevo)
    db.flush()
    _recalcular_puntaje_total(db, evaluacion)
    db.refresh(nuevo)
    return nuevo

def ActualizarPuntaje(db: Session, id_puntaje: int, datos: PuntajeCriterioActualizarSchema):
    puntaje = BuscarPuntaje(db, id_puntaje)
    if not puntaje:
        return None
    evaluacion = _validar_evaluacion_editable(db, puntaje.id_evaluacion)
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(puntaje, campo, valor)
    db.flush()
    _recalcular_puntaje_total(db, evaluacion)
    db.refresh(puntaje)
    return puntaje

def EliminarPuntaje(db: Session, id_puntaje: int):
    puntaje = BuscarPuntaje(db, id_puntaje)
    if not puntaje:
        return None
    evaluacion = _validar_evaluacion_editable(db, puntaje.id_evaluacion)
    db.delete(puntaje)
    db.flush()
    _recalcular_puntaje_total(db, evaluacion)
    return True