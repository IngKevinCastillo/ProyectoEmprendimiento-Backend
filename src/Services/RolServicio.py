from sqlalchemy.orm import Session
from fastapi import HTTPException
from decimal import Decimal
from datetime import datetime
from Models.RolesModelo import RolesModelo
from Schemas.Rolesschema import RolesCrearSchema

def BuscarRol(db: Session, id: int):
    return db.query(RolesModelo).filter(RolesModelo.id_rol == id).first()

def BuscarRolPorNombre(db: Session, nombre: str):
    return db.query(RolesModelo).filter(RolesModelo.nombre == nombre).first()

def ObtenerRoles(db: Session):
    return db.query(RolesModelo).all()

def CrearRol(db: Session, rol: RolesCrearSchema):
    existente = BuscarRolPorNombre(db, rol.nombre)
    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un tipo de rol con ese nombre")
    
    RolesModelo
    
    nuevo_rol = RolesModelo(
        nombre=rol.nombre, 
        estado=rol.estado
    )
    db.add(nuevo_rol)
    db.commit()
    db.refresh(nuevo_rol)
    return nuevo_rol

def EliminarRol(db: Session, id: int):
    rol = BuscarRol(db, id)
    if not rol:
        raise HTTPException(status_code=404, detail="No se encontró el tipo de rol")
    
    db.delete(rol)
    db.commit()
    return {"detail": "Tipo de rol eliminado"}

def ActualizarRol(db: Session, rolAActualizar: any):
    rol = BuscarRol(db, rolAActualizar.id_rol)
    if not rol:
        raise HTTPException(status_code=404, detail="No se encontró el tipo de rol")
    
    rol.nombre = rolAActualizar.nombre
    rol.estado = rolAActualizar.estado
    
    db.commit()
    db.refresh(rol)
    return rol