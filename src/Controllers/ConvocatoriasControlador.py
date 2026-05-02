from sqlalchemy.orm import Session
from Schemas.ConvocatoriasSchema import ConvocatoriasActualizarSchema, ConvocatoriasCrearSchema
from Services.ConvocatoriasServicio import actualizar_convocatoria, buscar_convocatoria, buscar_convocatoria_titulo, crear_convocatoria, eliminar_convocatoria, listar_convocatorias_por_estado, listar_convocatorias_por_tipo

def crear_convocatoria_controlador(db: Session, convocatoria: ConvocatoriasCrearSchema):
    return  crear_convocatoria(db, convocatoria)

def buscar_convocatoria_titulo_controlador(db: Session, titulo_convocatoria: str):
    return buscar_convocatoria_titulo(db, titulo_convocatoria)

def buscar_convocatoria_controlador(db: Session, id_convocatoria: int):
    return buscar_convocatoria(db, id_convocatoria)

def listar_convocatorias_por_tipo_controlador(db:Session, tipo_convocatoria: str):
    return listar_convocatorias_por_tipo(db, tipo_convocatoria)

def listar_convocatorias_por_estado_controlador(db:Session, estado_convocatoria: str):
    return listar_convocatorias_por_estado(db, estado_convocatoria)

def actualizar_convocatoria_controlador(db: Session, id_convocatoria: int, convocatoria: ConvocatoriasActualizarSchema):
    return actualizar_convocatoria(db, id_convocatoria, convocatoria)

def eliminar_convocatoria_controlador(db: Session, id_convocatoria: int):
    return eliminar_convocatoria(db, id_convocatoria)