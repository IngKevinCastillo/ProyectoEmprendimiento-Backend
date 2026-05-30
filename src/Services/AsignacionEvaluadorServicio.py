from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.AsignacionEvaluadorModelo import AsignacionEvaluadorModelo
from Models.PostulacionModelo import PostulacionModelo
from Models.UsuarioModelo import UsuarioModelo
from Models.RolesModelo import RolesModelo
from Schemas.AsignacionEvaluadorSchema import AsignacionCrearSchema
from Models.PostulacionModelo import PostulacionModelo
from Models.ProyectoModelo import ProyectoModelo

ID_ESTADO_POSTULACION_ENVIADA = 27

def _validar_evaluador(db: Session, id_evaluador: int):
    usuario = db.query(UsuarioModelo).filter(
        UsuarioModelo.id_usuario == id_evaluador
    ).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evaluador no encontrado")
    rol = db.query(RolesModelo).filter(
        RolesModelo.id_rol == usuario.id_rol
    ).first()
    if not rol or rol.nombre.lower() != "evaluador":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no tiene el rol de evaluador"
        )
    return usuario

def _validar_postulacion(db: Session, id_postulacion: int):
    postulacion = db.query(PostulacionModelo).filter(
        PostulacionModelo.id_postulacion == id_postulacion
    ).first()
    if not postulacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Postulación no encontrada")
    if postulacion.id_estado != ID_ESTADO_POSTULACION_ENVIADA:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede asignar evaluador a postulaciones enviadas"
        )
    return postulacion

def ObtenerAsignacionesPorPostulacion(db: Session, id_postulacion: int):
    return db.query(AsignacionEvaluadorModelo).filter(
        AsignacionEvaluadorModelo.id_postulacion == id_postulacion
    ).all()

def ObtenerAsignacionesPorEvaluador(db: Session, id_evaluador: int):
    asignaciones = db.query(AsignacionEvaluadorModelo).filter(
        AsignacionEvaluadorModelo.id_evaluador == id_evaluador
    ).all()

    resultado = []
    for asignacion in asignaciones:
        postulacion = db.query(PostulacionModelo).filter(
            PostulacionModelo.id_postulacion == asignacion.id_postulacion
        ).first()
        proyecto = db.query(ProyectoModelo).filter(
            ProyectoModelo.id_proyecto == postulacion.id_proyecto
        ).first()
        resultado.append({
            "id_asignacion": asignacion.id_asignacion,
            "id_postulacion": asignacion.id_postulacion,
            "id_evaluador": asignacion.id_evaluador,
            "fecha_asignacion": asignacion.fecha_asignacion,
            "nombre_proyecto": proyecto.nombre_proyecto,
            "id_proyecto": proyecto.id_proyecto
        })
    return resultado

def BuscarAsignacion(db: Session, id_asignacion: int):
    return db.query(AsignacionEvaluadorModelo).filter(
        AsignacionEvaluadorModelo.id_asignacion == id_asignacion
    ).first()

def CrearAsignacion(db: Session, id_postulacion: int, datos: AsignacionCrearSchema):
    _validar_postulacion(db, id_postulacion)
    _validar_evaluador(db, datos.id_evaluador)

    existe = db.query(AsignacionEvaluadorModelo).filter(
        AsignacionEvaluadorModelo.id_postulacion == id_postulacion,
        AsignacionEvaluadorModelo.id_evaluador == datos.id_evaluador
    ).first()
    if existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este evaluador ya está asignado a esta postulación"
        )

    nueva = AsignacionEvaluadorModelo(
        id_postulacion=id_postulacion,
        id_evaluador=datos.id_evaluador
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def EliminarAsignacion(db: Session, id_asignacion: int):
    asignacion = BuscarAsignacion(db, id_asignacion)
    if not asignacion:
        return None
    if asignacion.evaluacion:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede eliminar una asignación que ya tiene evaluación registrada"
        )
    db.delete(asignacion)
    db.commit()
    return True

