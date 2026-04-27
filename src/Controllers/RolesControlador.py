from sqlalchemy.orm import Session
from Schemas.Rolesschema import RolesCrearSchema, RolesRespuestaSchema
from Services.RolServicio import CrearRol, ObtenerRoles, BuscarRol, EliminarRol, ActualizarRol, BuscarRolPorNombre

def crear_rol_controlador(db: Session, rol: RolesCrearSchema):
    return CrearRol(db, rol)

def obtener_roles_controlador(db: Session):
    return ObtenerRoles(db)

def buscar_rol_controlador(db: Session, rol_id: str):
    return BuscarRol(db, rol_id)

def eliminar_rol_controlador(db: Session, rol_id: str):
    return EliminarRol(db, rol_id)

def actualizar_rol_controlador(db: Session, rol_id: str, rol_actualizado: RolesCrearSchema):
    return ActualizarRol(db, rol_actualizado, rol_id)

def buscar_rol_por_nombre_controlador(db: Session, nombre: str):
    return BuscarRolPorNombre(db, nombre)