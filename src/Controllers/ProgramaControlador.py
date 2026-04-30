from sqlalchemy.orm import Session
from Services.ProgramaServicio import BuscarPrograma, BuscarProgramaPorNombre, ObtenerProgramas

def buscar_programa_controlador(db: Session, id_programa: str):
    return BuscarPrograma(db, id_programa)

def buscar_programa_nombre_controlador(db: Session, nombre: str):
    return BuscarProgramaPorNombre(db, nombre)

def obtener_programas_controlador(db:Session):
    return ObtenerProgramas(db)