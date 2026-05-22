from sqlalchemy.orm import Session
from Schemas.ProyectoSchema import ProyectoCrearSchema, ProyectoActualizarSchema
from Services.ProyectoServicio import crearEmprendimiento, buscarEmprendimiento, obtenerEmprendimientos, obtenerEmprendimientosPorEstado, eliminarEmprendimiento, actualizarEmprendimiento, buscarEmprendimientoPorNombre, obtenerEmprendimientosPorCategoria, crearEmprendimientoConVinculo, obtenerEmprendimientosPorTipoProyecto, obtenerEmprendimientosPorEscala

def crear_emprendimiento_controlador(db: Session, emprendimiento: ProyectoCrearSchema):
    return crearEmprendimiento(db, emprendimiento)

def crear_emprendimiento_con_vinculo_controlador(db: Session, emprendimiento: ProyectoCrearSchema, id_usuario: int):
    return crearEmprendimientoConVinculo(db, emprendimiento, id_usuario)

def obtener_emprendimientos_controlador(db: Session):
    return obtenerEmprendimientos(db)

def obtener_emprendimientos_por_estado_controlador(db: Session, id_estado: int):
    return obtenerEmprendimientosPorEstado(db, id_estado)

def obtener_emprendimientos_por_categoria_controlador(db: Session, id_categoria: int):
    return obtenerEmprendimientosPorCategoria(db, id_categoria)

def obtener_emprendimientos_por_tipo_proyecto_controlador(db: Session, id_tipo_proyecto: int):
    return obtenerEmprendimientosPorTipoProyecto(db, id_tipo_proyecto)

def obtener_emprendimientos_por_escala_controlador(db: Session, id_escala: int):
    return obtenerEmprendimientosPorEscala(db, id_escala)

def buscar_emprendimiento_controlador(db: Session, id_emprendimiento: str):
    return buscarEmprendimiento(db, id_emprendimiento)

def buscar_emprendimiento_por_nombre_controlador(db: Session, nombre: str):
    return buscarEmprendimientoPorNombre(db, nombre)

def eliminar_emprendimiento_controlador(db: Session, id_emprendimiento: str):
    return eliminarEmprendimiento(db, id_emprendimiento)

def actualizar_emprendimiento_controlador(db: Session, actualizado: ProyectoActualizarSchema, id_proyecto: str):
    return actualizarEmprendimiento(db, actualizado, id_proyecto)