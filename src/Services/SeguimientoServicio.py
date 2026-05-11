from datetime import datetime, timezone
from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.SeguimientoModelo import SeguimientoModelo
from Schemas.SeguimientoSchema import SeguimientoCrearSchema, SeguimientoRespuestaSchema, SeguimientoActualizarSchema
from Services.EstadosServicio import BuscarEstadosPorNombre
from Utils.Mapeadorutilidades import auto_mapear

def BuscarSeguimiento(db: Session, id: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.id_seguimiento_emprendimiento == int(id), SeguimientoModelo.id_estado != BuscarEstadosPorNombre(db, "Eliminado").id_estado).first()

def BuscarUltimoSeguimientoPorProyecto(db: Session, id_proyecto: int):
    return db.query(SeguimientoModelo)\
        .filter(SeguimientoModelo.id_proyecto == int(id_proyecto), SeguimientoModelo.id_estado != BuscarEstadosPorNombre(db, "Eliminado").id_estado)\
        .order_by(SeguimientoModelo.fecha_registro.desc())\
        .first()

def ObtenerSeguimientos(db: Session):
    estado = BuscarEstadosPorNombre(db, "Eliminado")
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.id_estado != estado.id_estado).all()

def ObtenerSeguimientosPorProyecto(db: Session, id_proyecto: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.id_proyecto == int(id_proyecto), SeguimientoModelo.id_estado != BuscarEstadosPorNombre(db, "Eliminado").id_estado).all()

def ObtenerSeguimientosPorEstado(db: Session, id_estado: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.id_estado == int(id_estado)).all()

def ObtenerSeguimientoPorUsuarioResponsable(db: Session, id: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.id_usuario_responsable == int(id), SeguimientoModelo.id_estado != BuscarEstadosPorNombre(db, "Eliminado").id_estado).all()

def ObtenerSeguimientoPorFecha(db: Session, fecha: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.fecha_registro == fecha, SeguimientoModelo.id_estado != BuscarEstadosPorNombre(db, "Eliminado").id_estado).all()

def CrearSeguimiento(db: Session, seguimiento: SeguimientoCrearSchema) -> SeguimientoModelo:

    if seguimiento.id_proyecto is None:
        raise HTTPException(status_code=400, detail="El id_proyecto es obligatorio")

    nuevo_seguimiento = SeguimientoModelo(
        id_proyecto=seguimiento.id_proyecto,
        observaciones=seguimiento.observaciones,
        id_usuario_responsable=seguimiento.id_usuario_responsable,
        id_estado=seguimiento.id_estado,
        avance_porcentaje=seguimiento.avance_porcentaje,
        fecha_registro=datetime.now(timezone.utc)
        # fecha_registro se asigna automáticamente (default=func.now() en el modelo)
    )
    db.add(nuevo_seguimiento)
    db.commit()
    db.refresh(nuevo_seguimiento)
    return nuevo_seguimiento

def EliminarSeguimiento(db: Session, id: int):
    seguimiento = BuscarSeguimiento(db, id)
    if not seguimiento:
        raise HTTPException(status_code=404, detail="No se encontró el seguimiento")

    estado = BuscarEstadosPorNombre(db, "Eliminado")
    if not estado:
        raise HTTPException(status_code=404, detail="No se encontró el estado 'Eliminado' en la base de datos")
    
    seguimiento.id_estado = estado.id_estado
    db.delete(seguimiento)
    db.commit()
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