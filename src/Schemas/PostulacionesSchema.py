from pydantic import BaseModel, field_validator
from datetime import datetime


class PostulacionesCrearSchema(BaseModel):
    id_convocatoria: int
    id_proyecto: int
    informacion_adicional: str
    id_plan_negocio: int

    @field_validator("id_convocatoria", "id_proyecto", "id_plan_negocio")
    @classmethod
    def validar_ids_positivos(cls, v: int) -> int:
        if v < 1 or v > 2147483647:
            raise ValueError("El ID debe ser un entero positivo válido (1 - 2147483647).")
        return v

    @field_validator("informacion_adicional")
    @classmethod
    def validar_informacion(cls, v: str) -> str:
        v = v.strip()
        if len(v) > 400:
            raise ValueError("La información adicional no puede superar los 400 caracteres.")
        return v


class PostulacionesRespuestaSchema(BaseModel):
    id_postulacion: int
    id_convocatoria: int
    id_proyecto: int
    informacion_adicional: str
    id_plan_negocio: int
    fecha_registro: datetime

    class Config:
        from_attributes = True