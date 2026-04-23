from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.UsuarioModelo import UsuarioModelo
from Core.Seguridad import Hashear_contrasena
from Services.UsuarioServicio import BuscarUsuarioPorDocumento

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
    nuevo_usuario.contrasena = Hashear_contrasena(nuevo_usuario.contrasena)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario