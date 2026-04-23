from Services.UsuarioServicio import BuscarUsuario, ActualizarUsuario, EliminarUsuario, ObtenerUsuarios, BuscarUsuarioPorDocumento

def BuscarUsuarioControlador(db, id: int):
    return BuscarUsuario(db, id)

def ActualizarUsuarioControlador(db, usuarioAActualizar: any):
    return ActualizarUsuario(db, usuarioAActualizar)

def EliminarUsuarioControlador(db, id: int):
    return EliminarUsuario(db, id)

def ObtenerUsuariosControlador(db):
    return ObtenerUsuarios(db)

def BuscarUsuarioPorDocumentoControlador(db, numero_documento: str):
    return BuscarUsuarioPorDocumento(db, numero_documento)