from sqlalchemy.orm import Session
from Schemas.Facultadschema import FacultadCrearSchema, FacultadActualizarSchema
from Services.FacultadServicio import CrearFacultad, ObtenerFacultades, BuscarFacultad, EliminarFacultad, ActualizarFacultad, BuscarFacultadPorNombre, BuscarProgramasPorFacultad

def crear_facultad_contolador(db: Session, facultad: FacultadCrearSchema):
    return CrearFacultad(db, facultad)

def obtener_facultades_contolador(db: Session):
    return ObtenerFacultades(db)

def obtener_programas_por_facultad_contolador(db: Session, id_facultad: str):
    return BuscarProgramasPorFacultad(db, id_facultad)

def buscar_facultad_contolador(db: Session, id_facultad: str):
    return BuscarFacultad(db, id_facultad)

def buscar_facultad_nombre_contolador(db: Session, nombre: str):
    return BuscarFacultadPorNombre(db, nombre)

def eliminar_facultad_contolador(db: Session, id_facultad: str):
    return EliminarFacultad(db, id_facultad)

def actualizar_facultad_contolador(db: Session, id_facultad: str, facultad: FacultadActualizarSchema):
    return ActualizarFacultad(db, id_facultad, facultad)