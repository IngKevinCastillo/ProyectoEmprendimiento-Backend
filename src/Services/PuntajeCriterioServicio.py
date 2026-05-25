from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.PuntajeCriterioModelo import PuntajeCriterioModelo
from Models.EvaluacionModelo import EvaluacionModelo
from Models.CriterioEvaluacionModelo import CriterioEvaluacionModelo
from Schemas.PuntajeCriterioSchema import PuntajeCriterioCrearSchema, PuntajeCriterioActualizarSchema

def _validar_evaluacion_editable(db: Session, id_evaluacion: int):
    evaluacion = db.query(EvaluacionModelo).filter(
        EvaluacionModelo.id_evaluacion == id_evaluacion
    ).first()
    if not evaluacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evaluación no encontrada")
    if evaluacion.estado == "completada":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pueden modificar puntajes de una evaluación completada"
        )
    return evaluacion

def _validar_criterio(db: Session, id_criterio: int, id_convocatoria: int):
    criterio = db.query(CriterioEvaluacionModelo).filter(
        CriterioEvaluacionModelo.id_criterio == id_criterio,
        CriterioEvaluacionModelo.id_convocatoria == id_convocatoria
    ).first()
    if not criterio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El criterio no pertenece a la convocatoria de esta evaluación"
        )
    return criterio

def _recalcular_puntaje_total(db: Session, evaluacion: EvaluacionModelo):
    puntajes = db.query(PuntajeCriterioModelo).filter(
        PuntajeCriterioModelo.id_evaluacion == evaluacion.id_evaluacion
    ).all()
    evaluacion.puntaje_total = sum(p.puntaje_obtenido for p in puntajes)
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

    id_convocatoria = evaluacion.asignacion.postulacion.id_convocatoria
    criterio = _validar_criterio(db, datos.id_criterio, id_convocatoria)

    existe = db.query(PuntajeCriterioModelo).filter(
        PuntajeCriterioModelo.id_evaluacion == id_evaluacion,
        PuntajeCriterioModelo.id_criterio == datos.id_criterio
    ).first()
    if existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este criterio ya tiene un puntaje registrado en esta evaluación"
        )

    if datos.puntaje_obtenido < 0 or datos.puntaje_obtenido > criterio.puntaje_maximo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El puntaje debe estar entre 0 y {criterio.puntaje_maximo}"
        )

    nuevo = PuntajeCriterioModelo(
        id_evaluacion=id_evaluacion,
        id_criterio=datos.id_criterio,
        puntaje_obtenido=datos.puntaje_obtenido,
        comentario=datos.comentario
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

    if datos.puntaje_obtenido is not None:
        criterio = db.query(CriterioEvaluacionModelo).filter(
            CriterioEvaluacionModelo.id_criterio == puntaje.id_criterio
        ).first()
        if datos.puntaje_obtenido < 0 or datos.puntaje_obtenido > criterio.puntaje_maximo:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El puntaje debe estar entre 0 y {criterio.puntaje_maximo}"
            )

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