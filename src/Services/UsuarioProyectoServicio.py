from sqlalchemy.orm import Session
from fastapi import HTTPException
from Utils.Mapeadorutilidades import auto_mapear
from Models.UsuarioProyectoModelo import UsuarioProyectoModelo
from Schemas.UsuarioProyectoSchema import UsuarioProyectoCrearSchema, UsuarioProyectoActualizarSchema
from Services.UsuarioServicio import BuscarUsuario
from Services.ProyectoServicio import buscarEmprendimiento
from Services.RolServicio import BuscarRolPorNombre

def CrearUsuarioProyecto(db: Session, usuario_proyecto: UsuarioProyectoCrearSchema):
    usuario = BuscarUsuario(db, usuario_proyecto.id_usuario)
    emprendimiento = buscarEmprendimiento(db, usuario_proyecto.id_proyecto)

    if not usuario:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")

    if not emprendimiento:
        raise HTTPException(status_code=404, detail="No se encontró el emprendimiento")

    nuevo_proyecto = UsuarioProyectoModelo(
        id_proyecto = usuario_proyecto.id_proyecto,
        id_usuario = usuario_proyecto.id_usuario,
        id_rol = usuario_proyecto.id_rol
    )
    db.add(nuevo_proyecto)
    db.commit()
    db.refresh(nuevo_proyecto)
    return nuevo_proyecto

def ListarUsuariosProyectos(db: Session):
    return db.query(UsuarioProyectoModelo).all()

def ListarUsuariosProyectosPorProyecto(db: Session, id_proyecto: str):
    return db.query(UsuarioProyectoModelo).filter(UsuarioProyectoModelo.id_proyecto == int(id_proyecto)).all()

def ListarProyectosPorUsuario(db: Session, id_usuario: str):
    return db.query(UsuarioProyectoModelo).filter(UsuarioProyectoModelo.id_usuario == int(id_usuario)).all()

def ListarProyectosPorUsuarioPropietario(db: Session, id_usuario: int):
    rol_propietario = BuscarRolPorNombre(db, "Propietario")
    if not rol_propietario:
        raise HTTPException(status_code=404, detail="No se encontró el rol 'Propietario' en la base de datos")
    return db.query(UsuarioProyectoModelo).filter(UsuarioProyectoModelo.id_usuario == id_usuario, UsuarioProyectoModelo.id_rol == rol_propietario.id_rol).all()

def ListarProyectosPorUsuarioEmpleado(db: Session, id_usuario: int):
    rol_empleado = BuscarRolPorNombre(db, "Empleado")
    if not rol_empleado:
        raise HTTPException(status_code=404, detail="No se encontró el rol 'Empleado' en la base de datos")
    return db.query(UsuarioProyectoModelo).filter(UsuarioProyectoModelo.id_usuario == id_usuario, UsuarioProyectoModelo.id_rol == rol_empleado.id_rol).all()

def BuscarUsuarioProyecto(db: Session, id_usuario_proyecto: str):
    return db.query(UsuarioProyectoModelo).filter(UsuarioProyectoModelo.id_usuario_proyecto == int(id_usuario_proyecto)).first()

def EliminarUsuarioProyecto(db: Session, id_usuario_proyecto: str):
    usuario_proyecto = BuscarUsuarioProyecto(db, id_usuario_proyecto)
    if not usuario_proyecto:
        raise HTTPException(status_code=404, detail="No se encontró la relación usuario-proyecto")

    db.delete(usuario_proyecto)
    db.commit()
    return {"detail": "Relación usuario-proyecto eliminada"}

def ActualizarUsuarioProyecto(db: Session, id_usuario_proyecto: str, usuario_proyecto: UsuarioProyectoActualizarSchema):
    existente = BuscarUsuarioProyecto(db, id_usuario_proyecto)
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró la relación usuario-proyecto")
    
    auto_mapear(existente, usuario_proyecto, excluir=["id_usuario_proyecto"])

    db.commit()
    db.refresh(existente)
    return existente