from Services.AutenticacionServicio import CrearUsuario

def CrearUsuarioControlador(db, usuario):
    return CrearUsuario(db, usuario)