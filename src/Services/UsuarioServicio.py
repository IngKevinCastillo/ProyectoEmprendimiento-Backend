from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.UsuarioModelo import UsuarioModelo
from Utils.Mapeadorutilidades import auto_mapear
from Models.UsuarioProyectoModelo import UsuarioProyectoModelo
from Schemas.Usuarioschema import UsuarioActualizarSchema, CambiarEstado
eliminado = 6

def buscar_usuario(db: Session, id: int):
    return db.query(UsuarioModelo).filter(UsuarioModelo.id_usuario == id).first()

def buscar_telefono(db:Session, telefono: str):
    return db.query(UsuarioModelo).filter(UsuarioModelo.telefono == telefono).first()

def buscar_usuario_por_correo(db: Session, correo: str):
    return db.query(UsuarioModelo).filter(UsuarioModelo.correo == correo).first()

def buscar_usuario_por_documento(db: Session, documento: int):
    return db.query(UsuarioModelo).filter(UsuarioModelo.numero_documento == str(documento)).first()

def listar_usuarios(db: Session):
    return db.query(UsuarioModelo).all()

def cambiar_estado(db: Session, documento: int, estado: CambiarEstado):
    existente = buscar_usuario_por_documento(db, documento)
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario especificado no existe.")
    
    existente.id_estado = estado.id_estado_cambiar
    
    db.commit()
    db.refresh(existente)
    return existente

def eliminar_usuario(db: Session, id: int):
    usuario = buscar_usuario(db, id)
    
    if not usuario:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")

    usuario.id_estado = eliminado

    db.commit()
    db.refresh(usuario)
    return {"detail": "Usuario eliminado"}

def actualizar_usuario_id(db: Session, usuario: UsuarioActualizarSchema, id_usuario: int):
    existente = buscar_usuario(db, id_usuario)
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")
    
    if(existente.id_rol is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un rol")
    
    if(existente.id_tipodocumento is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un tipo de documento")
    
    auto_mapear(existente, usuario, excluir=["id_usuario", "contrasena"])

    db.commit()
    db.refresh(existente)
    return existente

def actualizar_usuario_documento(db: Session, usuario: UsuarioActualizarSchema, documento: int):
    existente = buscar_usuario_por_documento(db, documento)
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")
    
    if(existente.id_rol is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un rol")
    
    if(existente.id_tipodocumento is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un tipo de documento")
    
    auto_mapear(existente, usuario, excluir=["id_usuario", "contrasena"])

    db.commit()
    db.refresh(existente)
    return existente