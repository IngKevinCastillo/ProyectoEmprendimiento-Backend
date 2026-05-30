from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import date
from Models.PostulacionModelo import PostulacionModelo
from Models.ConvocatoriaModelo import ConvocatoriaModelo
from Models.ProyectoModelo import ProyectoModelo
from Models.UsuarioProyectoModelo import UsuarioProyectoModelo
from Models.UsuarioModelo import UsuarioModelo
from Models.RolesModelo import RolesModelo
from Schemas.PostulacionSchema import PostulacionCrearSchema, PostulacionActualizarSchema

ID_ESTADO_ENVIADA = 27
ID_ESTADO_APROBADA = 4
ID_ESTADO_RECHAZADA = 15
ID_ESTADO_CONVOCATORIA_PUBLICADA = 19

def _validar_convocatoria_abierta(db: Session, id_convocatoria: int):
    convocatoria = db.query(ConvocatoriaModelo).filter(
        ConvocatoriaModelo.id_convocatoria == id_convocatoria
    ).first()
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatoria no encontrada")
    if convocatoria.id_estado != ID_ESTADO_CONVOCATORIA_PUBLICADA:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede postular a convocatorias publicadas"
        )
    if convocatoria.fecha_cierre < date.today():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La convocatoria ya cerró"
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

def BuscarPostulacion(db: Session, id_postulacion: int):
    return db.query(PostulacionModelo).filter(
        PostulacionModelo.id_postulacion == id_postulacion
    ).first()

def ObtenerPostulacionesPorConvocatoria(db: Session, id_convocatoria: int):
    return db.query(PostulacionModelo).filter(
        PostulacionModelo.id_convocatoria == id_convocatoria
    ).all()

def ObtenerPostulacionesPorProyecto(db: Session, id_proyecto: int):
    return db.query(PostulacionModelo).filter(
        PostulacionModelo.id_proyecto == id_proyecto
    ).all()

def CrearPostulacion(db: Session, id_convocatoria: int, datos: PostulacionCrearSchema):
    _validar_convocatoria_abierta(db, id_convocatoria)
    _validar_proyecto_existe(db, datos.id_proyecto)
    _validar_no_duplicado(db, id_convocatoria, datos.id_proyecto)
    nueva = PostulacionModelo(
        id_convocatoria=id_convocatoria,
        id_proyecto=datos.id_proyecto,
        respuestas=datos.respuestas,
        id_estado=ID_ESTADO_ENVIADA
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def ActualizarPostulacion(db: Session, id_postulacion: int, datos: PostulacionActualizarSchema):
    postulacion = BuscarPostulacion(db, id_postulacion)
    if not postulacion:
        return None
    if postulacion.id_estado != ID_ESTADO_ENVIADA:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede editar una postulación en estado enviada"
        )
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(postulacion, campo, valor)
    db.commit()
    db.refresh(postulacion)
    return postulacion

def CambiarEstadoPostulacion(db: Session, id_postulacion: int, id_estado: int):
    postulacion = BuscarPostulacion(db, id_postulacion)
    if not postulacion:
        return None
    if id_estado not in (ID_ESTADO_APROBADA, ID_ESTADO_RECHAZADA):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El estado debe ser aprobada o rechazada"
        )
    if postulacion.id_estado != ID_ESTADO_ENVIADA:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede cambiar el estado de una postulación enviada"
        )
    postulacion.id_estado = id_estado
    db.commit()
    db.refresh(postulacion)
    return postulacion

def EliminarPostulacion(db: Session, id_postulacion: int):
    postulacion = BuscarPostulacion(db, id_postulacion)
    if not postulacion:
        return None
    if postulacion.id_estado != ID_ESTADO_ENVIADA:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede eliminar una postulación en estado enviada"
        )
    db.delete(postulacion)
    db.commit()
    return True

def ObtenerIntegrantesPostulacion(db: Session, id_postulacion: int):
    postulacion = BuscarPostulacion(db, id_postulacion)
    if not postulacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Postulación no encontrada")

    rol_propietario = db.query(RolesModelo).filter(
        RolesModelo.nombre == "Propietario"
    ).first()
    if not rol_propietario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol Propietario no encontrado")

    usuario_proyectos = db.query(UsuarioProyectoModelo).filter(
        UsuarioProyectoModelo.id_proyecto == postulacion.id_proyecto
    ).all()

    propietario = None
    integrantes = []

    for up in usuario_proyectos:
        usuario = db.query(UsuarioModelo).filter(
            UsuarioModelo.id_usuario == up.id_usuario
        ).first()
        if not usuario:
            continue
        integrante = {
            "id_usuario": usuario.id_usuario,
            "primer_nombre": usuario.primer_nombre,
            "segundo_nombre": usuario.segundo_nombre,
            "primer_apellido": usuario.primer_apellido,
            "segundo_apellido": usuario.segundo_apellido,
            "correo": usuario.correo,
            "numero_documento": usuario.numero_documento,
            "telefono": usuario.telefono,
            "id_rol": up.id_rol
        }
        if up.id_rol == rol_propietario.id_rol:
            propietario = integrante
        else:
            integrantes.append(integrante)

    if not propietario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontró el propietario del proyecto"
        )

    return {
        "id_proyecto": postulacion.id_proyecto,
        "propietario": propietario,
        "integrantes": integrantes
    }