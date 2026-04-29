from sqlalchemy.orm import Session
from Schemas.EstadoProyectoSchema import EstadoProyectoCrearSchema, EstadoProyectoRespuestaSchema
from Services.EstadoProyectoServicio import BuscarEstadoProyecto, BuscarEstadoProyectoPorNombre, ObtenerEstadosProyectos, CrearEstadoProyecto, EliminarEstadoProyecto, ActualizarEstadoProyecto

def crear_estado_proyecto_controlador(db: Session, estado_proyecto: EstadoProyectoCrearSchema):
    return CrearEstadoProyecto(db, estado_proyecto)

def obtener_estados_proyectos_controlador(db: Session):
    return ObtenerEstadosProyectos(db)

def buscar_estado_proyecto_controlador(db: Session, id_estado_proyecto: str):
    return BuscarEstadoProyecto(db, id_estado_proyecto)

def obtener_estados_proyectos_por_nombre_controlador(db: Session, nombre: str):
    return BuscarEstadoProyectoPorNombre(db, nombre)

def eliminar_estado_proyecto_controlador(db: Session, id_estado_proyecto: str):
    return EliminarEstadoProyecto(db, id_estado_proyecto)

def actualizar_estado_proyecto_controlador(db: Session, id_estado_proyecto: str, actualizado: EstadoProyectoCrearSchema):
    return ActualizarEstadoProyecto(db, actualizado, id_estado_proyecto)


