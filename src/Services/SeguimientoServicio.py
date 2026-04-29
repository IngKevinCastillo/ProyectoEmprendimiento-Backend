from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.SeguimientoModelo import SeguimientoModelo
from Schemas.SeguimientoSchema import SeguimientoCrearSchema
from Utils.Mapeadorutilidades import auto_mapear

def BuscarSeguimiento(db: Session, id: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.id_seguimiento_emprendimiento == int(id)).first()

def BuscarSeguimientoPorEmprendimiento(db: Session, id: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.id_proyecto == int(id)).first()

def BuscarSeguimientoPorUsuarioResponsable(db: Session, id: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.id_usuario_responsable == int(id)).first()

def ObtenerSeguimientos(db: Session):
    return db.query(SeguimientoModelo).all()

def ObtenerSeguimientosPorEstado(db: Session, estado: str):
    return db.query(SeguimientoModelo).filter(SeguimientoModelo.id_estado_emprendimiento == int(estado)).first()

def CrearSeguimiento(db: Session, seguimiento: SeguimientoCrearSchema):

    existente = BuscarSeguimiento(db, seguimiento.id_estado_emprendimiento)

    if existente:
        raise HTTPException(status_code=400, detail="Este seguimiento ya existe")
    
    if(existente.id_proyecto is None):
        raise HTTPException(status_code=400, detail="El seguimiento debe estar asociado a un proyecto")
    
    if(existente.id_usuario_responsable is None):
        raise HTTPException(status_code=400, detail="El seguimiento debe presentar como minimo una persona responsable a cargo")

    if(existente.id_estado_emprendimiento is None):
        raise HTTPException(status_code=400, detail="El seguimiento debe sustentar el estado actual del emprendimiento")
      
    nuevo_seguimiento = SeguimientoModelo(
        id_proyecto = seguimiento.id_proyecto,
        observaciones = seguimiento.observaciones,
        id_usuario_responsable = seguimiento.id_usuario_responsable,
        id_estado_emprendimiento = seguimiento.id_estado_emprendimiento,
        avance_porcentaje = seguimiento.avance_porcentaje
    )
    db.add(nuevo_seguimiento)
    db.commit()
    db.refresh(nuevo_seguimiento)
    return nuevo_seguimiento

def EliminarSeguimiento(db: Session, id: int):
    seguimiento = BuscarSeguimiento(db, id)
    if not seguimiento:
        raise HTTPException(status_code=404, detail="No se encontró el seguimiento")

    db.delete(seguimiento)
    db.commit()
    return {"detail": "Seguimiento eliminado"}

def ActualizarSeguimiento(db: Session, seguimiento: any):
    existente = BuscarSeguimiento(db, seguimiento.id_usuario)
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró el seguimiento")
    
    auto_mapear(existente, seguimiento, excluir=["id_seguimiento_emprendimiento"])

    db.commit()
    db.refresh(existente)
    return existente