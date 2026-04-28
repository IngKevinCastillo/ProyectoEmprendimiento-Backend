from sqlalchemy.orm import Session
from Services.ProgramaServicio import ActualizarPrograma, BuscarPrograma, BuscarProgramaPorNombre, CrearPrograma, EliminarPrograma, ObtenerProgramas
from Schemas.Programaschema import ProgramaCrearSchema, ProgramaActualizarSchema

def crear_programa_controlador(db: Session, programa: ProgramaCrearSchema):
    return CrearPrograma(db, programa)

def buscar_programa_controlador(db: Session, id_programa: str):
    return BuscarPrograma(db, id_programa)

def buscar_programa_nombre_controlador(db: Session, nombre: str):
    return BuscarProgramaPorNombre(db, nombre)

def obtener_programas_controlador(db:Session):
    return ObtenerProgramas(db)

def eliminar_programa_controlador(db: Session, id_programa: str):
    return EliminarPrograma(db, id_programa)

def actualizar_programa_controlador(db: Session, programa: ProgramaActualizarSchema, id_programa: str):
    return ActualizarPrograma(db, programa, id_programa)