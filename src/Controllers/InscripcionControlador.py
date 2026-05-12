from sqlalchemy.orm import Session
from Services.InscripcionServicio import cambiar_estado, actualizar_inscripcion, buscar_inscripcion, crear_inscripcion, eliminar_inscripcion, listar_inscripciones_curso, listar_inscripciones_usuario, verificar_registro
from Schemas.InscripcionSchema import InscripcionCrearSchema, InscripcionActualizarSchema
from Schemas.EstadosSchema import CambiarEstado

def crear_inscripcion_controlador(db: Session, inscripcion: InscripcionCrearSchema):
    return crear_inscripcion(db, inscripcion)

def listar_inscripciones_curso_controlador(db: Session, id_curso: int):
    return listar_inscripciones_curso(db, id_curso)

def buscar_inscripcion_controlador(db: Session, id_inscripcion: int):
    return buscar_inscripcion(db, id_inscripcion)

def listar_inscripciones_usuario_controlador(db: Session, id_usuario: int):
    return listar_inscripciones_usuario(db, id_usuario)

def verificar_registro_controlador(db: Session, id_usuario: int, id_curso: int):
    return verificar_registro(db, id_usuario, id_curso)

def actualizar_inscripcion_controlador(db: Session, id_inscripcion: int, inscripcion: InscripcionActualizarSchema):
    return actualizar_inscripcion(db, id_inscripcion, inscripcion)

def eliminar_inscripcion_controlador(db: Session, id_inscripcion: int):
    return eliminar_inscripcion(db, id_inscripcion)

def cambiar_estado_controlador(db: Session, id_inscripcion: int, estado: CambiarEstado):
    return cambiar_estado(db, id_inscripcion, estado)