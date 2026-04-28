from sqlalchemy.orm import Session
from Schemas.UsuarioProyectoSchema import UsuarioProyectoCrearSchema,UsuarioProyectoActualizarSchema
from Services.UsuarioProyectoServicio import CrearUsuarioProyecto, ListarUsuariosProyectos, BuscarUsuarioProyecto, EliminarUsuarioProyecto, ActualizarUsuarioProyecto

def crear_usuario_proyecto_controlador(db: Session, usuario_proyecto: UsuarioProyectoCrearSchema):
    return CrearUsuarioProyecto(db, usuario_proyecto)

def listar_usuarios_proyectos_controlador(db: Session):
    return ListarUsuariosProyectos(db)

def buscar_usuario_proyecto_controlador(db: Session, id_usuario_proyecto: str):
    return BuscarUsuarioProyecto(db, id_usuario_proyecto)

def eliminar_usuario_proyecto_controlador(db: Session, id_usuario_proyecto: str):
    return EliminarUsuarioProyecto(db, id_usuario_proyecto)

def actualizar_usuario_proyecto_controlador(db: Session, id_usuario_proyecto: str, usuario_proyecto: UsuarioProyectoActualizarSchema):
    return ActualizarUsuarioProyecto(db, id_usuario_proyecto, usuario_proyecto)