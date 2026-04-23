from Services.UsuarioServicio import BuscarUsuario, ActualizarUsuario, EliminarUsuario, ObtenerUsuarios, BuscarUsuarioPorDocumento

def BuscarUsuarioControlador(db, id):
    return BuscarUsuario(db, id)

def ActualizarUsuarioControlador(db, usuarioAActualizar):
    return ActualizarUsuario(db, usuarioAActualizar)

def EliminarUsuarioControlador(db, id):
    return EliminarUsuario(db, id)

def ObtenerUsuariosControlador(db):
    return ObtenerUsuarios(db)

def BuscarUsuarioPorDocumentoControlador(db, numero_documento):
    return BuscarUsuarioPorDocumento(db, numero_documento)