from sqlalchemy.orm import Session
from fastapi import HTTPException
from decimal import Decimal
from datetime import datetime
from Models.UsuarioModelo import UsuarioModelo
from Models.FacultadModelo import FacultadModelo
from Models.ProgramaModelo import  ProgramaModelo
from Models.RolesModelo import RolesModelo
from Models.TipoDocumentoModelo import TipoDocumentoModelo

def BuscarUsuario(db: Session, id: int):
    return db.query(UsuarioModelo).filter(UsuarioModelo.id_usuario == id).first()

def BuscarUsuarioPorDocumento(db: Session, nombre: str):
    return db.query(UsuarioModelo).filter(UsuarioModelo.numero_documento == nombre).first()

def ObtenerUsuarios(db: Session):
    return db.query(UsuarioModelo).all()

def CrearUsuario(db: Session, usuario: any):
    existente = BuscarUsuarioPorDocumento(db, usuario.numero_documento)
    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un usuario con esa número de documento")
    
    if(usuario.id_rol is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un rol")
    
    if(usuario.id_tipodocumento is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un tipo de documento")

    campos = [
        "id_usuario",
        "primer_nombre", "segundo_nombre",
        "primer_apellido", "segundo_apellido",
        "correo", "contrasena",
        "id_rol", "fecha_registro", "estado",
        "fecha_nacimiento", "ubicacion_semestral",
        "sexo", "id_programa", "id_tipodocumento",
        "numero_documento", "telefono", "id_facultad"
    ]

    data = {campo: getattr(usuario, campo) for campo in campos}

    nuevo_usuario = UsuarioModelo(**data)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def EliminarUsuario(db: Session, id: int):
    usuario = BuscarUsuario(db, id)
    if not usuario:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")

    db.delete(usuario)
    db.commit()
    return {"detail": "Usuario eliminado"}

def ActualizarUsuario(db: Session, usuarioAActualizar: any):
    usuario = BuscarUsuario(db, usuarioAActualizar.id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")
    
    if(usuario.id_rol is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un rol")
    
    if(usuario.id_tipodocumento is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un tipo de documento")
    
    for campo in [
        "primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido",
        "correo", "contrasena", "id_rol", "fecha_registro", "estado",
        "fecha_nacimiento", "ubicacion_semestral", "sexo",
        "id_programa", "id_tipodocumento", 
        "numero_documento", "telefono", "id_facultad"
    ]:
        setattr(usuario, campo, getattr(usuarioAActualizar, campo))

    db.commit()
    db.refresh(usuario)
    return usuario