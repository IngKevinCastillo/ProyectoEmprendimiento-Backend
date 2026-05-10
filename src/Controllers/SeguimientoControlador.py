from sqlalchemy.orm import Session
from Schemas.SeguimientoSchema import SeguimientoCrearSchema, SeguimientoRespuestaSchema, SeguimientoActualizarSchema
from Services.SeguimientoServicio import CrearSeguimiento, BuscarSeguimiento, ObtenerSeguimientosPorProyecto, ObtenerSeguimientoPorUsuarioResponsable, EliminarSeguimiento, ActualizarSeguimiento, ObtenerSeguimientos, ObtenerSeguimientosPorEstado, BuscarUltimoSeguimientoPorProyecto

def crear_seguimiento_controlador(db: Session, seguimiento: SeguimientoCrearSchema):
    return CrearSeguimiento(db, seguimiento)

def obtener_seguimientos_controlador(db: Session):
    return ObtenerSeguimientos(db)

def obtener_seguimientos_por_estado_controlador(db: Session, estado: str):
    return ObtenerSeguimientosPorEstado(db, estado)

def obtener_seguimiento_por_usuario_responsable_controlador(db: Session, id_usuario_responsable: str):
    return ObtenerSeguimientoPorUsuarioResponsable(db, id_usuario_responsable)

def obtener_seguimientos_por_proyecto_controlador(db: Session, id_proyecto: str):
    return ObtenerSeguimientosPorProyecto(db, id_proyecto)

def buscar_seguimiento_controlador(db: Session, id_seguimiento: str):
    return BuscarSeguimiento(db, id_seguimiento)

def buscar_ultimo_seguimiento_por_proyecto_controlador(db: Session, id_proyecto: int):
    return BuscarUltimoSeguimientoPorProyecto(db, id_proyecto)

def eliminar_seguimiento_controlador(db: Session, id_seguimiento: str):
    return EliminarSeguimiento(db, id_seguimiento)

def actualizar_seguimiento_controlador(db: Session, id_seguimiento: str, actualizado: SeguimientoActualizarSchema):
    return ActualizarSeguimiento(db, id_seguimiento, actualizado)


