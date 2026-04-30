from sqlalchemy.orm import Session
from Services.RolServicio import ObtenerRoles, BuscarRol, BuscarRolPorNombre

def obtener_roles_controlador(db: Session):
    return ObtenerRoles(db)

def buscar_rol_controlador(db: Session, rol_id: str):
    return BuscarRol(db, rol_id)

def buscar_rol_por_nombre_controlador(db: Session, nombre: str):
    return BuscarRolPorNombre(db, nombre)