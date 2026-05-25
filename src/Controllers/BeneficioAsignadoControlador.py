from sqlalchemy.orm import Session
from Schemas.BeneficioAsignadoSchema import BeneficioAsignadoCrearSchema, BeneficioAsignadoActualizarSchema
from Services.BeneficioAsignadoServicio import (ObtenerBeneficiosAsignadosPorConvocatoria, ObtenerBeneficiosAsignadosPorProyecto, BuscarBeneficioAsignado, CrearBeneficioAsignado, ActualizarBeneficioAsignado, CambiarEstadoBeneficioAsignado, EliminarBeneficioAsignado)

def obtener_beneficios_asignados_por_convocatoria_controlador(db: Session, id_convocatoria: int):
    return ObtenerBeneficiosAsignadosPorConvocatoria(db, id_convocatoria)

def obtener_beneficios_asignados_por_proyecto_controlador(db: Session, id_proyecto: int):
    return ObtenerBeneficiosAsignadosPorProyecto(db, id_proyecto)

def buscar_beneficio_asignado_controlador(db: Session, id_beneficio_asignado: int):
    return BuscarBeneficioAsignado(db, id_beneficio_asignado)

def crear_beneficio_asignado_controlador(db: Session, id_convocatoria: int, datos: BeneficioAsignadoCrearSchema, id_admin: int):
    return CrearBeneficioAsignado(db, id_convocatoria, datos, id_admin)

def actualizar_beneficio_asignado_controlador(db: Session, id_beneficio_asignado: int, datos: BeneficioAsignadoActualizarSchema):
    return ActualizarBeneficioAsignado(db, id_beneficio_asignado, datos)

def cambiar_estado_beneficio_asignado_controlador(db: Session, id_beneficio_asignado: int, nuevo_estado: str):
    return CambiarEstadoBeneficioAsignado(db, id_beneficio_asignado, nuevo_estado)

def eliminar_beneficio_asignado_controlador(db: Session, id_beneficio_asignado: int):
    return EliminarBeneficioAsignado(db, id_beneficio_asignado)