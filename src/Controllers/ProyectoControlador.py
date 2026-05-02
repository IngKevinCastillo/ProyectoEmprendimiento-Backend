from sqlalchemy.orm import Session
from Schemas.ProyectoSchema import ProyectoCrearSchema, ProyectoRespuestaSchema
from Services.ProyectoServicio import crearEmprendimiento, buscarEmprendimiento, obtenerEmprendimientos, obtenerEmprendimientosPorEstado, eliminarEmprendimiento, actualizarEmprendimiento, buscarEmprendimientoPorNombre

def crear_emprendimiento_controlador(db: Session, emprendimiento: ProyectoCrearSchema):
    return crearEmprendimiento(db, emprendimiento)

def obtener_emprendimientos_controlador(db: Session):
    return obtenerEmprendimientos(db)

def obtener_emprendimientos_por_estado_controlador(db: Session, id_estado_proyecto: int):
    return obtenerEmprendimientosPorEstado(db, id_estado_proyecto)

def buscar_emprendimiento_controlador(db: Session, id_emprendimiento: str):
    return buscarEmprendimiento(db, id_emprendimiento)

def buscar_emprendimiento_por_nombre_controlador(db: Session, nombre: str):
    return buscarEmprendimientoPorNombre(db, nombre)

def eliminar_emprendimiento_controlador(db: Session, id_emprendimiento: str):
    return eliminarEmprendimiento(db, id_emprendimiento)

def actualizar_emprendimiento_controlador(db: Session, actualizado: ProyectoCrearSchema):
    return actualizarEmprendimiento(db, actualizado)


