from Services.UsuarioServicio import RecuperarContrasena, CambiarContrasena, CambiarCorreo, buscar_usuario, buscar_telefono, actualizar_usuario_id, actualizar_usuario_documento, eliminar_usuario, buscar_usuario_por_correo, buscar_usuario_por_documento, cambiar_estado, listar_usuarios
from sqlalchemy.orm import Session
from Schemas.Usuarioschema import UsuarioActualizarSchema
from Schemas.EstadosSchema import CambiarEstado

def BuscarUsuarioControlador(db: Session, id: int):
    return buscar_usuario(db, id)

def BuscarUsuarioPorCorreoControlador(db: Session, correo: str):
    return buscar_usuario_por_correo(db, correo)

def BuscarUsuarioPorTelefonoControlador(db: Session, id: int):
    return buscar_telefono(db, id)

def ActualizarUsuarioIdControlador(db: Session, usuarioAActualizar: UsuarioActualizarSchema, id_usuario: int):
    return actualizar_usuario_id(db, usuarioAActualizar, id_usuario)

def ActualizarUsuarioDocumentoControlador(db: Session, usuarioAActualizar: UsuarioActualizarSchema, documento: int):
    return actualizar_usuario_documento(db, usuarioAActualizar, documento)

def EliminarUsuarioControlador(db: Session, numero_documento: int):
    return eliminar_usuario(db, numero_documento)

def ObtenerUsuariosControlador(db: Session):
    return listar_usuarios(db)

def BuscarUsuarioPorDocumentoControlador(db: Session, numero_documento: int):
    return buscar_usuario_por_documento(db, numero_documento)

def CambiarEstadoControlador(db, documento: int, estado: CambiarEstado):
    return cambiar_estado(db, documento, estado)

def CambiarCorreoControlador(db: Session, correo_actual: str, correo_nuevo: str):
    return CambiarCorreo(db, correo_actual, correo_nuevo)

def CambiarContrasenaControlador(db: Session, correo: str, contasena_anterior: str, contrasena_nueva: str):
    return CambiarContrasena(db, correo, contasena_anterior, contrasena_nueva)

def RecuperarContrasenaControlador(db: Session, correo: str, contrasena_nueva: str):
    return RecuperarContrasena(db, correo, contrasena_nueva)