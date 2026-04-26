from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.UsuarioModelo import UsuarioModelo

def BuscarUsuario(db: Session, id: int):
    return db.query(UsuarioModelo).filter(UsuarioModelo.id_usuario == id).first()

def BuscarUsuarioPorCorreo(db: Session, correo: str):
    return db.query(UsuarioModelo).filter(UsuarioModelo.correo == correo).first()

def BuscarUsuarioPorDocumento(db: Session, documento: str):
    return db.query(UsuarioModelo).filter(UsuarioModelo.numero_documento == documento).first()

def ObtenerUsuarios(db: Session):
    return db.query(UsuarioModelo).all()

def EliminarUsuario(db: Session, id: int):
    usuario = BuscarUsuario(db, id)
    if not usuario:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")

    db.delete(usuario)
    db.commit()
    return {"detail": "Usuario eliminado"}

def ActualizarUsuario(db: Session, usuario: any):
    existente = BuscarUsuario(db, usuario.id_usuario)
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")
    
    if(existente.id_rol is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un rol")
    
    if(existente.id_tipodocumento is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un tipo de documento")
    
    for campo in [
        "primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido",
        "correo", "contrasena", "id_rol", "fecha_registro", "estado",
        "fecha_nacimiento", "ubicacion_semestral", "sexo",
        "id_programa", "id_tipodocumento", 
        "numero_documento", "telefono", "id_facultad"
    ]:
        setattr(existente, campo, getattr(usuario, campo))

    db.commit()
    db.refresh(existente)
    return existente