from Services.AutenticacionServicio import CrearUsuario, IniciarSesion, CambiarContrasena
from sqlalchemy.orm import Session
from Schemas.Usuarioschema import UsuarioCrearSchema

def CrearUsuarioControlador(db: Session, usuario: UsuarioCrearSchema):
    return CrearUsuario(db, usuario)

def IniciarSesionControlador(db: Session, datos: UsuarioCrearSchema):
    return IniciarSesion(datos, db)

def CambiarContrasenaControlador(db: Session, id_usuario: int, contasena_anterior: str, contrasena_nueva: str):
    return CambiarContrasena(db, id_usuario, contasena_anterior, contrasena_nueva)