from sqlalchemy.orm import Session
from Models.RolesModelo import RolesModelo

def BuscarRol(db: Session, id_rol: str):
    return db.query(RolesModelo).filter(RolesModelo.id_rol == int(id_rol)).first()

def BuscarRolPorNombre(db: Session, nombre: str):
    return db.query(RolesModelo).filter(RolesModelo.nombre == nombre).first()

def ObtenerRoles(db: Session):
    return db.query(RolesModelo).all()