from sqlalchemy.orm import Session
from Schemas.SeguimientoSchema import SeguimientoCrearSchema, SeguimientoRespuestaSchema
from Services.SeguimientoServicio import CrearSeguimiento, BuscarSeguimiento, BuscarSeguimientoPorEmprendimiento, BuscarSeguimientoPorUsuarioResponsable, EliminarSeguimiento, ActualizarSeguimiento, ObtenerSeguimientos, ObtenerSeguimientosPorEstado

def crear_seguimiento_controlador(db: Session, seguimiento: SeguimientoCrearSchema):
    return CrearSeguimiento(db, seguimiento)

def obtener_seguimientos_controlador(db: Session):
    return ObtenerSeguimientos(db)

def obtener_seguimientos_por_estado_controlador(db: Session, estado: str):
    return ObtenerSeguimientosPorEstado(db, estado)

def buscar_seguimiento_controlador(db: Session, id_seguimiento: str):
    return BuscarSeguimiento(db, id_seguimiento)

def buscar_seguimiento_por_emprendimiento_controlador(db: Session, id_emprendimiento: str):
    return BuscarSeguimientoPorEmprendimiento(db, id_emprendimiento)

def buscar_seguimiento_por_usuario_responsable_controlador(db: Session, id_usuario_responsable: str):
    return BuscarSeguimientoPorUsuarioResponsable(db, id_usuario_responsable)

def eliminar_seguimiento_controlador(db: Session, id_emprendimiento: str):
    return EliminarSeguimiento(db, id_emprendimiento)

def actualizar_emprendimiento_controlador(db: Session, actualizado: SeguimientoCrearSchema):
    return ActualizarSeguimiento(db, actualizado)


