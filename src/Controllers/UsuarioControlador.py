from Services.UsuarioServicio import BuscarUsuario, ActualizarUsuario, EliminarUsuario, ObtenerUsuarios, BuscarUsuarioPorDocumento, EmprendimientosUsuario
from sqlalchemy.orm import Session
from Schemas.Usuarioschema import UsuarioCrearSchema, UsuarioActualizarSchema

def BuscarUsuarioControlador(db: Session, id: int):
    return BuscarUsuario(db, id)

def ActualizarUsuarioControlador(db: Session, usuarioAActualizar: UsuarioActualizarSchema, id_usuario: str):
    return ActualizarUsuario(db, usuarioAActualizar, id_usuario)

def EliminarUsuarioControlador(db: Session, id: int):
    return EliminarUsuario(db, id)

def ObtenerUsuariosControlador(db: Session):
    return ObtenerUsuarios(db)

def BuscarUsuarioPorDocumentoControlador(db: Session, numero_documento: str):
    return BuscarUsuarioPorDocumento(db, numero_documento)

def EmprendimientosUsuarioControlador(db: Session, id_usuario: str):
    return EmprendimientosUsuario(db, id_usuario)