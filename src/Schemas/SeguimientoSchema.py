from pydantic import BaseModel, field_validator
from datetime import date
from decimal import Decimal


class SeguimientoCrearSchema(BaseModel):
    id_proyecto: int
    observaciones: str
    id_usuario_responsable: int
    id_estado_proyecto: int
    avance_porcentaje: Decimal

    @field_validator("id_proyecto", "id_usuario_responsable", "id_estado_proyecto")
    @classmethod
    def validar_ids_positivos(cls, v: int) -> int:
        if v < 1 or v > 2147483647:
            raise ValueError("El ID debe ser un entero positivo válido (1 - 2147483647).")
        return v

    @field_validator("observaciones")
    @classmethod
    def validar_observaciones(cls, v: str) -> str:
        v = v.strip()
        if len(v) > 400 or not v:
            raise ValueError("Las observaciones deben tener entre 1 y 400 caracteres.")
        return v

    @field_validator("avance_porcentaje")
    @classmethod
    def validar_avance(cls, v: Decimal) -> Decimal:
        if v < Decimal("0.00") or v > Decimal("100.00"):
            raise ValueError("El avance debe estar entre 0.00 y 100.00.")
        return v


class SeguimientoRespuestaSchema(BaseModel):
    id_seguimiento_emprendimiento: int
    id_proyecto: int
    observaciones: str
    id_usuario_responsable: int
    fecha_registro: date
    id_estado_proyecto: int
    avance_porcentaje: Decimal

    class Config:
        from_attributes = True