from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.UsuarioModelo import UsuarioModelo
from Utils.Mapeadorutilidades import auto_mapear

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
    
    auto_mapear(existente, usuario, excluir=["id_usuario"])

    db.commit()
    db.refresh(existente)
    return existente