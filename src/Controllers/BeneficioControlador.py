from sqlalchemy.orm import Session
from Schemas.BeneficioSchema import BeneficioCrearSchema, BeneficioActualizarSchema
from Services.BeneficioServicio import (ObtenerBeneficios, BuscarBeneficio, CrearBeneficio, ActualizarBeneficio, EliminarBeneficio)

def obtener_beneficios_controlador(db: Session):
    return ObtenerBeneficios(db)

def buscar_beneficio_controlador(db: Session, id_beneficio: int):
    return BuscarBeneficio(db, id_beneficio)

def crear_beneficio_controlador(db: Session, datos: BeneficioCrearSchema):
    return CrearBeneficio(db, datos)

def actualizar_beneficio_controlador(db: Session, id_beneficio: int, datos: BeneficioActualizarSchema):
    return ActualizarBeneficio(db, id_beneficio, datos)

def eliminar_beneficio_controlador(db: Session, id_beneficio: int):
    return EliminarBeneficio(db, id_beneficio)