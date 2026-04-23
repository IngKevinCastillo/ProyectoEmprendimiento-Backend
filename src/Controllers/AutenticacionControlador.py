from Services.AutenticacionServicio import CrearUsuario, IniciarSesion
from sqlalchemy.orm import Session
from Schemas.Usuarioschema import UsuarioCrearSchema

def CrearUsuarioControlador(db: Session, usuario: UsuarioCrearSchema):
    return CrearUsuario(db, usuario)

def IniciarSesionControlador(db: Session, datos: UsuarioCrearSchema):
    return IniciarSesion(datos, db)