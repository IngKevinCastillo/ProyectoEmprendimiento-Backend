from Services.AutenticacionServicio import CrearUsuario, IniciarSesion

def CrearUsuarioControlador(db, usuario):
    return CrearUsuario(db, usuario)

def IniciarSesionControlador(db, datos):
    return IniciarSesion(datos, db)