from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.EvaluacionModelo import EvaluacionModelo
from Models.AsignacionEvaluadorModelo import AsignacionEvaluadorModelo
from Models.CriterioEvaluacionModelo import CriterioEvaluacionModelo
from Models.PuntajeCriterioModelo import PuntajeCriterioModelo
from Schemas.EvaluacionSchema import EvaluacionCrearSchema

ID_ESTADO_PENDIENTE = 13
ID_ESTADO_COMPLETADA = 28

def _validar_asignacion(db: Session, id_asignacion: int):
    asignacion = db.query(AsignacionEvaluadorModelo).filter(
        AsignacionEvaluadorModelo.id_asignacion == id_asignacion
    ).first()
    if not asignacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asignación no encontrada")
    return asignacion

def _validar_criterios_completos(db: Session, id_evaluacion: int):
    total_criterios = db.query(CriterioEvaluacionModelo).count()
    total_puntajes = db.query(PuntajeCriterioModelo).filter(
        PuntajeCriterioModelo.id_evaluacion == id_evaluacion
    ).count()
    if total_puntajes < total_criterios:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Faltan {total_criterios - total_puntajes} criterio(s) por calificar"
        )

def BuscarEvaluacion(db: Session, id_evaluacion: int):
    return db.query(EvaluacionModelo).filter(
        EvaluacionModelo.id_evaluacion == id_evaluacion
    ).first()

def BuscarEvaluacionPorAsignacion(db: Session, id_asignacion: int):
    return db.query(EvaluacionModelo).filter(
        EvaluacionModelo.id_asignacion == id_asignacion
    ).first()

def CrearEvaluacion(db: Session, id_asignacion: int, datos: EvaluacionCrearSchema):
    _validar_asignacion(db, id_asignacion)
    existe = BuscarEvaluacionPorAsignacion(db, id_asignacion)
    if existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Esta asignación ya tiene una evaluación registrada"
        )
    nueva = EvaluacionModelo(
        id_asignacion=id_asignacion,
        comentario_general=datos.comentario_general,
        puntaje_total=0.00,
        id_estado=ID_ESTADO_PENDIENTE
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def ActualizarComentario(db: Session, id_evaluacion: int, datos: EvaluacionCrearSchema):
    evaluacion = BuscarEvaluacion(db, id_evaluacion)
    if not evaluacion:
        return None
    if evaluacion.id_estado == ID_ESTADO_COMPLETADA:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede editar una evaluación ya completada"
        )
    evaluacion.comentario_general = datos.comentario_general
    db.commit()
    db.refresh(evaluacion)
    return evaluacion

def CompletarEvaluacion(db: Session, id_evaluacion: int):
    evaluacion = BuscarEvaluacion(db, id_evaluacion)
    if not evaluacion:
        return None
    if evaluacion.id_estado == ID_ESTADO_COMPLETADA:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La evaluación ya está completada"
        )
    _validar_criterios_completos(db, id_evaluacion)
    evaluacion.id_estado = ID_ESTADO_COMPLETADA
    db.commit()
    db.refresh(evaluacion)
    return evaluacion