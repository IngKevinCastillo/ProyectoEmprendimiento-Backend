from Services.AutenticacionServicio import CrearUsuario

def CrearUsuarioControlador(db, usuario: any):
    return CrearUsuario(db, usuario)