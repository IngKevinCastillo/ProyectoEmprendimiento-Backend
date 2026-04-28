from sqlalchemy.orm import Session
from Schemas.Facultadschema import FacultadCrearSchema, FacultadActualizarSchema
from Services.FacultadServicio import CrearFacultad, ObtenerFacultades, BuscarFacultad, EliminarFacultad, ActualizarFacultad, BuscarFacultadPorNombre

def crear_facultad(db: Session, facultad: FacultadCrearSchema):
    return CrearFacultad(db, facultad)

def obtener_facultades(db: Session):
    return ObtenerFacultades(db)

def buscar_facultad(db: Session, id_facultad: str):
    return BuscarFacultad(db, id_facultad)

def buscar_facultad_nombre(db: Session, nombre: str):
    return BuscarFacultadPorNombre(db, nombre)

def eliminar_facultad(db: Session, id_facultad: str):
    return EliminarFacultad(db, id_facultad)

def actualizar_facultad(db: Session, id_facultad: str, facultad: FacultadActualizarSchema):
    return ActualizarFacultad(db, id_facultad, facultad)