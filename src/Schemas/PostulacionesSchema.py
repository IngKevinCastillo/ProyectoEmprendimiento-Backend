from pydantic import BaseModel, field_validator, validation_info
from datetime import date
from Utils.Validacionesutilidades import validar_id_entero, validar_descripcion_utils

class PostulacionesCrearSchema(BaseModel):
    id_convocatoria: int
    id_proyecto: int
    informacion_adicional: str
    id_plan_negocio: int
    fecha_registro: date
    
    @field_validator("id_convocatoria", "id_proyecto", "id_plan_negocio")
    @classmethod
    def validar_ids_positivos(cls, v: int, info: validation_info) -> int:
        campo = info.field_name.replace("_", " ").capitalize()
        return validar_id_entero(v, campo=campo)

    @field_validator("informacion_adicional")
    @classmethod
    def validar_informacion_adicional(cls, v: str) -> str:
        return validar_descripcion_utils(v, min_len=20, max_len=2000, campo="Información adicional")

class PostulacionesRespuestaSchema(BaseModel):
    id_postulacion: int
    id_convocatoria: int
    id_proyecto: int
    informacion_adicional: str
    id_plan_negocio: int
    fecha_registro: date

    class Config:
        from_attributes = True

class PostulacionesActualizarSchema(BaseModel):
    id_convocatoria: int
    id_proyecto: int
    informacion_adicional: str
    id_plan_negocio: int