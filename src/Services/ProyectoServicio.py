from datetime import date
from typing import Final
from sqlalchemy.orm import Session
from fastapi import HTTPException
from Schemas.ProyectoSchema import ProyectoCrearSchema, ProyectoActualizarSchema
from Schemas.UsuarioProyectoSchema import UsuarioProyectoCrearSchema
from Models.ProyectoModelo import ProyectoModelo
from Core.CacheResolver import obtener_id_rol
from Services.UsuarioProyectoServicio import CrearUsuarioProyecto
from Utils.Mapeadorutilidades import auto_mapear

ESTADO_ELIMINADO: Final = "Eliminado"

def buscarEmprendimiento(db: Session, id: str):
    return db.query(ProyectoModelo).filter(ProyectoModelo.id_proyecto == int(id), ProyectoModelo.estado != ESTADO_ELIMINADO).first()

def buscarEmprendimientoPorNombre(db: Session, nombre: str):
    return db.query(ProyectoModelo).filter(ProyectoModelo.nombre_proyecto == nombre, ProyectoModelo.estado != ESTADO_ELIMINADO).first()

def obtenerEmprendimientos(db: Session):
    return db.query(ProyectoModelo).filter(ProyectoModelo.estado != ESTADO_ELIMINADO).all()

def obtenerEmprendimientosPorEstado(db: Session, estadoEntrante: str):
    return db.query(ProyectoModelo).filter(ProyectoModelo.estado == estadoEntrante).all()

def obtenerEmprendimientosPorCategoria(db: Session, categoria: str):
    return db.query(ProyectoModelo).filter(ProyectoModelo.id_categoria == int(categoria), ProyectoModelo.estado != ESTADO_ELIMINADO).all()

def obtenerEmprendimientosPorTipoProyecto(db: Session, tipo_proyecto: str):
    return db.query(ProyectoModelo).filter(ProyectoModelo.id_tipo_proyecto == int(tipo_proyecto), ProyectoModelo.estado != ESTADO_ELIMINADO).all()

def obtenerEmprendimientosPorEscala(db: Session, escala: str):
    return db.query(ProyectoModelo).filter(ProyectoModelo.id_escala == int(escala), ProyectoModelo.estado != ESTADO_ELIMINADO).all()

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

def crearEmprendimientoConVinculo(db: Session, emprendimiento: ProyectoCrearSchema, id_usuario: int):
    existente = buscarEmprendimientoPorNombre(db, emprendimiento.nombre_proyecto)
    rol_propietario = obtener_id_rol(db, "Propietario")

    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un proyecto con ese nombre")
    
    nuevo_emprendimiento = ProyectoModelo()
    auto_mapear(nuevo_emprendimiento, emprendimiento, excluir=["id_proyecto"])
    nuevo_emprendimiento.fecha_creacion = date.today()

    if nuevo_emprendimiento is None:
        raise HTTPException(status_code=400, detail="Ocurrio un error al crear el proyecto")
    
    db.add(nuevo_emprendimiento)
    db.commit()
    db.refresh(nuevo_emprendimiento)
    
    if not rol_propietario:
        raise HTTPException(status_code=404, detail="No se encontró el rol 'Propietario'")

    vinculo = UsuarioProyectoCrearSchema(
        id_proyecto=nuevo_emprendimiento.id_proyecto,
        id_usuario=id_usuario,
        id_rol=rol_propietario
    )

    CrearUsuarioProyecto(db, vinculo)
    return nuevo_emprendimiento

def eliminarEmprendimiento(db: Session, id: int):
    
    emprendimiento = buscarEmprendimiento(db, id)
    if not emprendimiento:
        raise HTTPException(status_code=404, detail="No se encontró el emprendimiento")

    emprendimiento.estado = ESTADO_ELIMINADO
    db.commit()
    db.refresh(emprendimiento)
    return {"detail": "Emprendimiento eliminado"}

def actualizarEmprendimiento(db: Session, emprendimiento: ProyectoActualizarSchema, id_proyecto: str):
    existente = buscarEmprendimiento(db, int(id_proyecto))

    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró el emprendimiento")
    
    datos_a_actualizar = emprendimiento.model_dump(exclude_unset=True)

    for nombre_campo, valor_campo in datos_a_actualizar.items():
        setattr(existente, nombre_campo, valor_campo)

    db.commit()
    db.refresh(existente)
    return existente