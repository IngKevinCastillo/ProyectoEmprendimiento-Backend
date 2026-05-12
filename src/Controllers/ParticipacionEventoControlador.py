from sqlalchemy.orm import Session
from Services.ParticipacionEventoServicio import cambiar_estado, actualizar_participacion_evento, buscar_participacion_evento, buscar_usuario_participacion_evento, buscar_usuario_participaciones_eventos, eliminar_participacion_proyecto, crear_participacion_evento, listar_participaciones_en_evento
from Schemas.ParticipacionEventoSchema import ParticipacionActualizarSchema, ParticipacionEventoCrearSchema
from Schemas.EstadosSchema import CambiarEstado

def crear_participacion_evento_controlador(db: Session, participacion_evento: ParticipacionEventoCrearSchema):
    return crear_participacion_evento(db, participacion_evento)

def buscar_participacion_evento_controlador(db: Session, id_participacion_evento: int):
    return buscar_participacion_evento(db, id_participacion_evento)

def buscar_usuario_participacion_evento_controlador(db: Session, id_usuario: int, id_evento: int):
    return buscar_usuario_participacion_evento(db, id_usuario, id_evento)

def buscar_usuarios_participaciones_eventos_controlador(db: Session, id_usuario: int):
    return buscar_usuario_participaciones_eventos(db, id_usuario)

def listar_participaciones_en_evento_controlador(db: Session, id_evento: int):
    return listar_participaciones_en_evento(db, id_evento)

def actualizar_participacion_evento_controlador(db: Session, id_participacion_evento: int, participacion_evento: ParticipacionActualizarSchema):
    return actualizar_participacion_evento(db, id_participacion_evento, participacion_evento)

def eliminar_participacion_proyecto_controlador(db: Session, id_participacion_evento: int):
    return eliminar_participacion_proyecto(db, id_participacion_evento)

def cambiar_estado_controlador(db: Session, id_participacion_evento: int, estado: CambiarEstado):
    return cambiar_estado(db, id_participacion_evento, estado)