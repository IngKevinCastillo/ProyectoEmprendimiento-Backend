from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.EstadoEmprendimientoModelos import EstadoEmprendimientoModelo
from Schemas.EstadoEmprendimientoSchema import EstadoEmprendimientoCrearSchema
from Utils.Mapeadorutilidades import auto_mapear

def BuscarEstadoEmprendimiento(db: Session, id_estado_emprendimiento: str):
    return db.query(EstadoEmprendimientoModelo).filter(EstadoEmprendimientoModelo.id_estado_emprendimiento == int(id_estado_emprendimiento)).first()

def BuscarEstadoEmprendimientoPorNombre(db: Session, nombre: str):
    return db.query(EstadoEmprendimientoModelo).filter(EstadoEmprendimientoModelo.nombre == nombre).first()

def ObtenerEstadosEmprendimientos(db: Session):
    return db.query(EstadoEmprendimientoModelo).all()

def CrearEstadoEmprendimiento(db: Session, estadoEmprendimiento: EstadoEmprendimientoCrearSchema):

    existente = BuscarEstadoEmprendimientoPorNombre(db, estadoEmprendimiento.nombre)

    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un estado de emprendimiento con ese nombre")
    
    EstadoEmprendimientoModelo
    
    nuevo_estado = EstadoEmprendimientoModelo(
        nombre=estadoEmprendimiento.nombre
    )
    db.add(nuevo_estado)
    db.commit()
    db.refresh(nuevo_estado)
    return nuevo_estado

def EliminarEstadoEmprendimiento(db: Session, id_estado_emprendimiento: str):
    existente = BuscarEstadoEmprendimiento(db, int(id_estado_emprendimiento))
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró ese estado de emprendimiento")
    
    db.delete(existente)
    db.commit()
    return {"detail": "Estado de emprendimiento eliminado"}

def ActualizarEstadoEmprendimiento(db: Session, estado_emprendimiento: any, id_estado_emprendimiento: str):
    existente = BuscarEstadoEmprendimiento(db, int(id_estado_emprendimiento))
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró ese estado de emprendimiento")
    
    auto_mapear(existente, estado_emprendimiento)
    
    db.commit()
    db.refresh(existente)
    return existente