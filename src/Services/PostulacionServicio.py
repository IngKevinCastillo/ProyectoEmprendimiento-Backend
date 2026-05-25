from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.PostulacionModelo import PostulacionModelo
from Models.ConvocatoriaModelo import ConvocatoriaModelo
from Models.ProyectoModelo import ProyectoModelo
from Schemas.PostulacionSchema import PostulacionCrearSchema, PostulacionActualizarSchema

TRANSICIONES_VALIDAS = {
    "borrador": ["enviada"],
    "enviada": ["en_revision"],
    "en_revision": ["aprobada", "rechazada"],
    "aprobada": [],
    "rechazada": []
}

def _validar_convocatoria_abierta(db: Session, id_convocatoria: int):
    convocatoria = db.query(ConvocatoriaModelo).filter(
        ConvocatoriaModelo.id_convocatoria == id_convocatoria
    ).first()
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatoria no encontrada")
    if convocatoria.estado != "publicada":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede postular a convocatorias publicadas"
        )
    return convocatoria

def _validar_proyecto_existe(db: Session, id_proyecto: int):
    proyecto = db.query(ProyectoModelo).filter(
        ProyectoModelo.id_proyecto == id_proyecto
    ).first()
    if not proyecto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proyecto no encontrado")
    return proyecto

def _validar_no_duplicado(db: Session, id_convocatoria: int, id_proyecto: int):
    existe = db.query(PostulacionModelo).filter(
        PostulacionModelo.id_convocatoria == id_convocatoria,
        PostulacionModelo.id_proyecto == id_proyecto
    ).first()
    if existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este proyecto ya tiene una postulación en esta convocatoria"
        )

def ObtenerPostulacionesPorConvocatoria(db: Session, id_convocatoria: int):
    return db.query(PostulacionModelo).filter(
        PostulacionModelo.id_convocatoria == id_convocatoria
    ).all()

def ObtenerPostulacionesPorProyecto(db: Session, id_proyecto: int):
    return db.query(PostulacionModelo).filter(
        PostulacionModelo.id_proyecto == id_proyecto
    ).all()

def BuscarPostulacion(db: Session, id_postulacion: int):
    return db.query(PostulacionModelo).filter(
        PostulacionModelo.id_postulacion == id_postulacion
    ).first()

def CrearPostulacion(db: Session, id_convocatoria: int, datos: PostulacionCrearSchema):
    _validar_convocatoria_abierta(db, id_convocatoria)
    _validar_proyecto_existe(db, datos.id_proyecto)
    _validar_no_duplicado(db, id_convocatoria, datos.id_proyecto)

    nueva = PostulacionModelo(
        id_convocatoria=id_convocatoria,
        id_proyecto=datos.id_proyecto,
        respuestas=datos.respuestas,
        estado="borrador"
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def ActualizarPostulacion(db: Session, id_postulacion: int, datos: PostulacionActualizarSchema):
    postulacion = BuscarPostulacion(db, id_postulacion)
    if not postulacion:
        return None
    if postulacion.estado != "borrador":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede editar una postulación en estado borrador"
        )
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(postulacion, campo, valor)
    db.commit()
    db.refresh(postulacion)
    return postulacion

def CambiarEstadoPostulacion(db: Session, id_postulacion: int, nuevo_estado: str):
    postulacion = BuscarPostulacion(db, id_postulacion)
    if not postulacion:
        return None
    estados_permitidos = TRANSICIONES_VALIDAS.get(postulacion.estado, [])
    if nuevo_estado not in estados_permitidos:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se puede pasar de '{postulacion.estado}' a '{nuevo_estado}'"
        )
    postulacion.estado = nuevo_estado
    db.commit()
    db.refresh(postulacion)
    return postulacion

def EliminarPostulacion(db: Session, id_postulacion: int):
    postulacion = BuscarPostulacion(db, id_postulacion)
    if not postulacion:
        return None
    if postulacion.estado != "borrador":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede eliminar una postulación en estado borrador"
        )
    db.delete(postulacion)
    db.commit()
    return True