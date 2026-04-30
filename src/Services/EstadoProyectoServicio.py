from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.EstadoProyectoModelos import EstadoProyectoModelo
from Schemas.EstadoProyectoSchema import EstadoProyectoCrearSchema
from Utils.Mapeadorutilidades import auto_mapear

def BuscarEstadoProyecto(db: Session, id_estado_proyecto: str):
    return db.query(EstadoProyectoModelo).filter(EstadoProyectoModelo.id_estado_proyecto == int(id_estado_proyecto)).first()

def BuscarEstadoProyectoPorNombre(db: Session, nombre: str):
    return db.query(EstadoProyectoModelo).filter(EstadoProyectoModelo.nombre == nombre).first()

def ObtenerEstadosProyectos(db: Session):
    return db.query(EstadoProyectoModelo).all()

def CrearEstadoProyecto(db: Session, estado_proyecto: EstadoProyectoCrearSchema):

    existente = BuscarEstadoProyectoPorNombre(db, estado_proyecto.nombre)

    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un estado de Proyecto con ese nombre")

    nuevo_estado = EstadoProyectoModelo(
        nombre=estado_proyecto.nombre
    )
    db.add(nuevo_estado)
    db.commit()
    db.refresh(nuevo_estado)
    return nuevo_estado

def EliminarEstadoProyecto(db: Session, id_estado_proyecto: str):
    existente = BuscarEstadoProyecto(db, int(id_estado_proyecto))
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró ese estado de Proyecto")
    
    db.delete(existente)
    db.commit()
    return {"detail": "Estado de Proyecto eliminado"}

def ActualizarEstadoProyecto(db: Session, estado_proyecto: any, id_estado_proyecto: str):
    existente = BuscarEstadoProyecto(db, int(id_estado_proyecto))
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró ese estado de Proyecto")
    
    auto_mapear(existente, estado_proyecto, excluir=["id_estado_proyecto"])
    
    db.commit()
    db.refresh(existente)
    return existente