from sqlalchemy.orm import Session
from Services.FacultadServicio import ObtenerFacultades, BuscarFacultad, BuscarFacultadPorNombre, BuscarProgramasPorFacultad

def obtener_facultades_contolador(db: Session):
    return ObtenerFacultades(db)

def obtener_programas_por_facultad_contolador(db: Session, id_facultad: str):
    return BuscarProgramasPorFacultad(db, id_facultad)

def buscar_facultad_contolador(db: Session, id_facultad: str):
    return BuscarFacultad(db, id_facultad)

def buscar_facultad_nombre_contolador(db: Session, nombre: str):
    return BuscarFacultadPorNombre(db, nombre)