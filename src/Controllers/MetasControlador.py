from sqlalchemy.orm import Session
from Services.MetasServicio import buscarMeta, obtenerMetas, obtenerMetasPorAnio, obtenerMetasPorEstado, crearMeta, actualizarMeta, eliminarMeta

def buscar_meta_controlador(db: Session, id_meta: str):
    return buscarMeta(db, id_meta)

def obtener_metas_controlador(db: Session):
    return obtenerMetas(db)

def obtener_metas_por_anio_controlador(db: Session, anio: str):
    return obtenerMetasPorAnio(db, anio)

def obtener_metas_por_estado_controlador(db: Session, estado: str):
    return obtenerMetasPorEstado(db, estado)

def crear_meta_controlador(db: Session, meta):
    return crearMeta(db, meta)

def actualizar_meta_controlador(db: Session, id_meta: int, datos_actualizados):
    return actualizarMeta(db, id_meta, datos_actualizados)

def eliminar_meta_controlador(db: Session, id_meta: int):
    return eliminarMeta(db, id_meta)