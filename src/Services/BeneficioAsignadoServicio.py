from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.BeneficioAsignadoModelo import BeneficioAsignadoModelo
from Models.ConvocatoriaModelo import ConvocatoriaModelo
from Models.PostulacionModelo import PostulacionModelo
from Models.BeneficioModelo import BeneficioModelo
from Models.AsignacionEvaluadorModelo import AsignacionEvaluadorModelo
from Models.EvaluacionModelo import EvaluacionModelo
from Schemas.BeneficioAsignadoSchema import BeneficioAsignadoCrearSchema, BeneficioAsignadoActualizarSchema

ID_ESTADO_POSTULACION_APROBADA = 4
ID_ESTADO_EVALUACION_COMPLETADA = 28
ID_ESTADO_BENEFICIO_PENDIENTE = 13

TRANSICIONES_VALIDAS = {
    13: [27],   # pendiente → entregado
    27: [28],   # entregado → confirmado
    28: []      # confirmado
}

def _validar_convocatoria(db: Session, id_convocatoria: int):
    convocatoria = db.query(ConvocatoriaModelo).filter(
        ConvocatoriaModelo.id_convocatoria == id_convocatoria
    ).first()
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatoria no encontrada")
    return convocatoria

def _validar_proyecto_postulado(db: Session, id_convocatoria: int, id_proyecto: int):
    postulacion = db.query(PostulacionModelo).filter(
        PostulacionModelo.id_convocatoria == id_convocatoria,
        PostulacionModelo.id_proyecto == id_proyecto,
        PostulacionModelo.id_estado == ID_ESTADO_POSTULACION_APROBADA
    ).first()
    if not postulacion:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El proyecto no tiene una postulación aprobada en esta convocatoria"
        )

    asignaciones = db.query(AsignacionEvaluadorModelo).filter(
        AsignacionEvaluadorModelo.id_postulacion == postulacion.id_postulacion
    ).all()

    if not asignaciones:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La postulación no tiene evaluadores asignados"
        )

    for asignacion in asignaciones:
        evaluacion = db.query(EvaluacionModelo).filter(
            EvaluacionModelo.id_asignacion == asignacion.id_asignacion
        ).first()
        if not evaluacion or evaluacion.id_estado != ID_ESTADO_EVALUACION_COMPLETADA:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Todas las evaluaciones deben estar completadas antes de asignar beneficios"
            )
    return postulacion

def _validar_beneficio(db: Session, id_beneficio: int):
    beneficio = db.query(BeneficioModelo).filter(
        BeneficioModelo.id_beneficio == id_beneficio
    ).first()
    if not beneficio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Beneficio no encontrado")
    return beneficio

def ObtenerBeneficiosAsignadosPorConvocatoria(db: Session, id_convocatoria: int):
    return db.query(BeneficioAsignadoModelo).filter(
        BeneficioAsignadoModelo.id_convocatoria == id_convocatoria
    ).all()

def ObtenerBeneficiosAsignadosPorProyecto(db: Session, id_proyecto: int):
    return db.query(BeneficioAsignadoModelo).filter(
        BeneficioAsignadoModelo.id_proyecto == id_proyecto
    ).all()

def BuscarBeneficioAsignado(db: Session, id_beneficio_asignado: int):
    return db.query(BeneficioAsignadoModelo).filter(
        BeneficioAsignadoModelo.id_beneficio_asignado == id_beneficio_asignado
    ).first()

def CrearBeneficioAsignado(db: Session, id_convocatoria: int, datos: BeneficioAsignadoCrearSchema, id_admin: int):
    _validar_convocatoria(db, id_convocatoria)
    _validar_proyecto_postulado(db, id_convocatoria, datos.id_proyecto)
    _validar_beneficio(db, datos.id_beneficio)
    nuevo = BeneficioAsignadoModelo(
        id_convocatoria=id_convocatoria,
        id_proyecto=datos.id_proyecto,
        id_beneficio=datos.id_beneficio,
        descripcion_entrega=datos.descripcion_entrega,
        id_estado=ID_ESTADO_BENEFICIO_PENDIENTE,
        asignado_por=id_admin
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def ActualizarBeneficioAsignado(db: Session, id_beneficio_asignado: int, datos: BeneficioAsignadoActualizarSchema):
    beneficio_asignado = BuscarBeneficioAsignado(db, id_beneficio_asignado)
    if not beneficio_asignado:
        return None
    if beneficio_asignado.id_estado != ID_ESTADO_BENEFICIO_PENDIENTE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede editar un beneficio asignado en estado pendiente"
        )
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(beneficio_asignado, campo, valor)
    db.commit()
    db.refresh(beneficio_asignado)
    return beneficio_asignado

def CambiarEstadoBeneficioAsignado(db: Session, id_beneficio_asignado: int, nuevo_estado: int):
    beneficio_asignado = BuscarBeneficioAsignado(db, id_beneficio_asignado)
    if not beneficio_asignado:
        return None
    estados_permitidos = TRANSICIONES_VALIDAS.get(beneficio_asignado.id_estado, [])
    if nuevo_estado not in estados_permitidos:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Transición de estado no permitida"
        )
    beneficio_asignado.id_estado = nuevo_estado
    db.commit()
    db.refresh(beneficio_asignado)
    return beneficio_asignado

def EliminarBeneficioAsignado(db: Session, id_beneficio_asignado: int):
    beneficio_asignado = BuscarBeneficioAsignado(db, id_beneficio_asignado)
    if not beneficio_asignado:
        return None
    if beneficio_asignado.id_estado != ID_ESTADO_BENEFICIO_PENDIENTE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede eliminar un beneficio asignado en estado pendiente"
        )
    db.delete(beneficio_asignado)
    db.commit()
    return True