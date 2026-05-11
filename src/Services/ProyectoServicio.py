from datetime import date
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Schemas.ProyectoSchema import ProyectoCrearSchema, ProyectoActualizarSchema
from Models.ProyectoModelo import ProyectoModelo
from Models.UsuarioProyectoModelo import UsuarioProyectoModelo
from Utils.Mapeadorutilidades import auto_mapear
eliminado = 6

def buscarEmprendimiento(db: Session, id: str):
    return db.query(ProyectoModelo).filter(ProyectoModelo.id_proyecto == int(id)).first()

def buscarEmprendimientoPorNombre(db: Session, nombre: str):
    return db.query(ProyectoModelo).filter(ProyectoModelo.nombre_proyecto == nombre).first()

def obtenerEmprendimientos(db: Session):
    return db.query(ProyectoModelo).all()

def obtenerEmprendimientosPorEstado(db: Session, estado: str):
    return db.query(ProyectoModelo).filter(ProyectoModelo.id_estado == int(estado)).all()

def obtenerEmprendimientosPorCategoria(db: Session, categoria: str):
    return db.query(ProyectoModelo).filter(ProyectoModelo.id_categoria == int(categoria)).all()

def crearEmprendimiento(db: Session, emprendimiento: ProyectoCrearSchema):
    existente = buscarEmprendimientoPorNombre(db, emprendimiento.nombre_proyecto)

    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un proyecto con ese nombre")
    
    nuevo_emprendimiento = ProyectoModelo()
    auto_mapear(nuevo_emprendimiento, emprendimiento, excluir=["id_proyecto"])
    nuevo_emprendimiento.fecha_creacion = date.today()
    
    db.add(nuevo_emprendimiento)
    db.commit()
    db.refresh(nuevo_emprendimiento)
    return nuevo_emprendimiento

def eliminarEmprendimiento(db: Session, id: int):
    emprendimiento = buscarEmprendimiento(db, id)
    
    if not emprendimiento:
        raise HTTPException(status_code=404, detail="No se encontró el proyecto")

    if(emprendimiento.id_estado == eliminado):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El proyecto no existe")

    emprendimiento.id_estado = eliminado

    db.commit()
    db.refresh(emprendimiento)
    return {"detail": "Emprendimiento eliminado"}

def actualizarEmprendimiento(db: Session, emprendimiento: ProyectoActualizarSchema, id_proyecto: str):
    existente = buscarEmprendimiento(db, int(id_proyecto))

    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró el emprendimiento")
    
    if existente.id_estado is None:
        raise HTTPException(status_code=400, detail="El emprendimiento debe estar asociado a un estado")
    
    if existente.id_categoria is None:
        raise HTTPException(status_code=400, detail="El emprendimiento debe estar asociado a una categoría")
    
    datos_a_actualizar = emprendimiento.model_dump(exclude_unset=True)

    for nombre_campo, valor_campo in datos_a_actualizar.items():
        setattr(existente, nombre_campo, valor_campo)

    db.commit()
    db.refresh(existente)
    return existente