from sqlalchemy.orm import Session
from fastapi import HTTPException
from Utils.Mapeadorutilidades import auto_mapear
from Models.UsuarioProyectoModelo import UsuarioProyectoModelo
from Schemas.UsuarioProyectoSchema import UsuarioProyectoCrearSchema, UsuarioProyectoActualizarSchema
from Services.UsuarioServicio import BuscarUsuario

def CrearUsuarioProyecto(db: Session, usuario_proyecto: UsuarioProyectoCrearSchema):
    usuario = BuscarUsuario(db, usuario_proyecto.id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")

    nuevo_proyecto = UsuarioProyectoModelo(
        id_usuario=usuario_proyecto.id_usuario,
        id_proyecto=usuario_proyecto.id_proyecto,
        rol_en_proyecto=usuario_proyecto.rol_en_proyecto
    )
    db.add(nuevo_proyecto)
    db.commit()
    db.refresh(nuevo_proyecto)
    return nuevo_proyecto

def ListarUsuariosProyectos(db: Session):
    return db.query(UsuarioProyectoModelo).all()

def BuscarUsuarioProyecto(db: Session, id_usuario_proyecto: str):
    return db.query(UsuarioProyectoModelo).filter(UsuarioProyectoModelo.id_usuario_proyecto == int(id_usuario_proyecto)).first()

def EliminarUsuarioProyecto(db: Session, id_usuario_proyecto: str):
    usuario_proyecto = BuscarUsuarioProyecto(db, id_usuario_proyecto)
    if not usuario_proyecto:
        raise HTTPException(status_code=404, detail="No se encontró la relación usuario-proyecto")

    db.delete(usuario_proyecto)
    db.commit()
    return {"detail": "Relación usuario-proyecto eliminada"}

def ActualizarUsuarioProyecto(db: Session, id_usuario_proyecto: str, usuario_proyecto_actualizado: UsuarioProyectoActualizarSchema):
    existente = BuscarUsuarioProyecto(db, id_usuario_proyecto)
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró la relación usuario-proyecto")
    
    auto_mapear(existente, usuario_proyecto_actualizado, excluir=["id_usuario_proyecto"])

    db.commit()
    db.refresh(existente)
    return existente