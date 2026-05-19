from Services.AutenticacionServicio import CrearUsuario, IniciarSesion, crear_usuario_supabase_service
from sqlalchemy.orm import Session
from Schemas.Usuarioschema import UsuarioCrearSchema
from Services.UsuarioServicio import CambiarContrasena

def CrearUsuarioControlador(db: Session, usuario: UsuarioCrearSchema):
    nuevo_usuario = CrearUsuario(db, usuario)
    crear_usuario_supabase_service(usuario.correo, usuario.contrasena)
    return nuevo_usuario

def IniciarSesionControlador(db: Session, datos: UsuarioCrearSchema):
    return IniciarSesion(datos, db)