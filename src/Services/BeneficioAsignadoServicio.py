from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.BeneficioAsignadoModelo import BeneficioAsignadoModelo
from Models.ConvocatoriaModelo import ConvocatoriaModelo
from Models.PostulacionModelo import PostulacionModelo
from Models.BeneficioModelo import BeneficioModelo
from Models.ProyectoModelo import ProyectoModelo
from Schemas.BeneficioAsignadoSchema import BeneficioAsignadoCrearSchema, BeneficioAsignadoActualizarSchema

TRANSICIONES_VALIDAS = {
    "pendiente": ["entregado"],
    "entregado": ["confirmado"],
    "confirmado": []
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
        PostulacionModelo.estado == "aprobada"
    ).first()
    if not postulacion:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El proyecto no tiene una postulación aprobada en esta convocatoria"
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
        estado="pendiente",
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
    if beneficio_asignado.estado != "pendiente":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede editar un beneficio asignado en estado pendiente"
        )
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(beneficio_asignado, campo, valor)
    db.commit()
    db.refresh(beneficio_asignado)
    return beneficio_asignado

def CambiarEstadoBeneficioAsignado(db: Session, id_beneficio_asignado: int, nuevo_estado: str):
    beneficio_asignado = BuscarBeneficioAsignado(db, id_beneficio_asignado)
    if not beneficio_asignado:
        return None
    estados_permitidos = TRANSICIONES_VALIDAS.get(beneficio_asignado.estado, [])
    if nuevo_estado not in estados_permitidos:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se puede pasar de '{beneficio_asignado.estado}' a '{nuevo_estado}'"
        )
    beneficio_asignado.estado = nuevo_estado
    db.commit()
    db.refresh(beneficio_asignado)
    return beneficio_asignado

def EliminarBeneficioAsignado(db: Session, id_beneficio_asignado: int):
    beneficio_asignado = BuscarBeneficioAsignado(db, id_beneficio_asignado)
    if not beneficio_asignado:
        return None
    if beneficio_asignado.estado != "pendiente":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede eliminar un beneficio asignado en estado pendiente"
        )
    db.delete(beneficio_asignado)
    db.commit()
    return True