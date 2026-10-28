from datetime import datetime, timezone
from typing import Final
from sqlalchemy import Date, and_, cast, func
from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.SeguimientoModelo import SeguimientoModelo
from Schemas.SeguimientoSchema import SeguimientoCrearSchema, SeguimientoActualizarSchema
from Core.CacheResolver import obtener_nombre_mesa_por_id
from Utils.Mapeadorutilidades import auto_mapear

ESTADO_ELIMINADO: Final = "Eliminado"
MESA_FINAL: Final = 4

def BuscarSeguimiento(db: Session, id: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.id_seguimiento_emprendimiento == int(id), SeguimientoModelo.estado != ESTADO_ELIMINADO).first()

def BuscarUltimoSeguimientoPorProyecto(db: Session, id_proyecto: int):
    return db.query(SeguimientoModelo)\
        .filter(SeguimientoModelo.id_proyecto == int(id_proyecto), SeguimientoModelo.estado != ESTADO_ELIMINADO)\
        .order_by(SeguimientoModelo.fecha_registro.desc())\
        .first()

def ObtenerSeguimientos(db: Session):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.estado != ESTADO_ELIMINADO).all()

def ObtenerUltimoSeguimientoDeCadaProyecto(db: Session):
    subquery_max_fecha = db.query(SeguimientoModelo.id_proyecto, func.max(SeguimientoModelo.fecha_registro).label("ultima_fecha"))\
        .filter(SeguimientoModelo.estado != ESTADO_ELIMINADO)\
        .group_by(
            SeguimientoModelo.id_proyecto
        )\
        .subquery("max_fechas")
    return db.query(SeguimientoModelo).join(subquery_max_fecha, and_(SeguimientoModelo.id_proyecto == subquery_max_fecha.c.id_proyecto, SeguimientoModelo.fecha_registro == subquery_max_fecha.c.ultima_fecha)).all()

def ObtenerSeguimientosPorProyecto(db: Session, id_proyecto: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.id_proyecto == int(id_proyecto), SeguimientoModelo.estado != ESTADO_ELIMINADO).all()

def ObtenerSeguimientosPorEstado(db: Session, estado: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.estado == estado).all()

def ObtenerSeguimientoPorUsuarioResponsable(db: Session, id: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.id_usuario_responsable == int(id), SeguimientoModelo.estado != ESTADO_ELIMINADO).all()

def ObtenerSeguimientoPorFecha(db: Session, fecha: str):
    fecha_dt = datetime.strptime(fecha, "%d-%m-%Y").date()
    return db.query(SeguimientoModelo).filter(cast(SeguimientoModelo.fecha_registro, Date) == fecha_dt, SeguimientoModelo.estado != ESTADO_ELIMINADO).all()

def ObtenerSeguimientosPorMesas(db: Session, id_mesas: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.id_mesas == int(id_mesas), SeguimientoModelo.estado != ESTADO_ELIMINADO).all()

def ValidarMesaPermitida(db: Session, id_proyecto: int, id_mesa_solicitada: int) -> None:
    ultimo = BuscarUltimoSeguimientoPorProyecto(db, id_proyecto)

    if ultimo is None:
        if id_mesa_solicitada != 1:
            raise HTTPException(status_code=400, detail="El primer seguimiento de un proyecto debe registrarse en la mesa Diagnostica.")
        return
    
    if not ultimo.transferir_mesa:
        if id_mesa_solicitada != ultimo.id_mesas:
            actual = obtener_nombre_mesa_por_id(db, ultimo.id_mesas) if ultimo else "Ninguna"
            raise HTTPException(status_code=400,
                detail=(
                    f"El proyecto continúa en la mesa {actual}. "
                    "Para avanzar a la siguiente, el seguimiento anterior "
                    "debe marcar 'transferir_mesa' en verdadero."
                ),
            )
    else:
        if ultimo.id_mesas >= MESA_FINAL:
            raise HTTPException(
                status_code=400,
                detail="El proyecto ya se encuentra en la mesa final y no puede avanzar a una siguiente."
            )
        
        mesa_esperada = ultimo.id_mesas + 1
        if id_mesa_solicitada != mesa_esperada:
            esperada = obtener_nombre_mesa_por_id(db, mesa_esperada)
            solicitante = obtener_nombre_mesa_por_id(db, id_mesa_solicitada)
            raise HTTPException(status_code=400,
                detail=(
                    f"La mesa anterior autorizó la transferencia. "
                    f"El próximo seguimiento debe registrarse en la mesa {esperada}, "
                    f"no en la mesa {solicitante}."
                ),
            )

def CrearSeguimiento(db: Session, seguimiento: SeguimientoCrearSchema) -> SeguimientoModelo:

    if seguimiento.id_proyecto is None:
        raise HTTPException(status_code=400, detail="El id_proyecto es obligatorio")
    
    ValidarMesaPermitida(db, seguimiento.id_proyecto, seguimiento.id_mesas)    

    nuevo_seguimiento = SeguimientoModelo()
    auto_mapear(nuevo_seguimiento, seguimiento, excluir=["id_seguimiento_emprendimiento"])
    nuevo_seguimiento.fecha_registro = datetime.now(timezone.utc)
    
    db.add(nuevo_seguimiento)
    db.commit()
    db.refresh(nuevo_seguimiento)
    return nuevo_seguimiento

def EliminarSeguimiento(db: Session, id: int):
    seguimiento = BuscarSeguimiento(db, id)
    if not seguimiento:
        raise HTTPException(status_code=404, detail="No se encontró el seguimiento")
    
    seguimiento.estado = ESTADO_ELIMINADO
    db.commit()
    db.refresh(seguimiento)
    return {"detail": "Seguimiento eliminado"}

def ActualizarSeguimiento(db: Session, id_seguimiento: str, datos_actualizados: SeguimientoActualizarSchema):
    existente = BuscarSeguimiento(db, id_seguimiento)

    if not existente:
        raise HTTPException(status_code=404, detail="Seguimiento no encontrado")

    datos_a_actualizar = datos_actualizados.model_dump(exclude_unset=True)

    for nombre_campo, valor_campo in datos_a_actualizar.items():
        setattr(existente, nombre_campo, valor_campo)

    db.commit()
    db.refresh(existente)
    return existente