from typing import Optional
from pydantic import BaseModel, field_validator, ValidationInfo
from datetime import datetime
from decimal import Decimal
from Utils.Validacionesutilidades import validar_id_entero 

class SeguimientoBaseSchema(BaseModel):
    id_proyecto: Optional[int] = None
    observaciones: Optional[str] = None
    id_usuario_responsable: Optional[int] = None
    id_estado: Optional[int] = None
    avance_porcentaje: Optional[Decimal] = None

    @field_validator("id_proyecto", "id_usuario_responsable", "id_estado")
    @classmethod
    def validar_ids_positivos(cls, v: int, info: ValidationInfo) -> int:
        campo = info.field_name.replace("_", " ").capitalize()
        return validar_id_entero(v, campo=campo)

    @field_validator("observaciones")
    @classmethod
    def validar_observaciones(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        if len(v) > 400 or not v:
            raise ValueError("Las observaciones deben tener entre 1 y 400 caracteres.")
        return v

    @field_validator("avance_porcentaje")
    @classmethod
    def validar_avance(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        if v is None:
            return v
        if v < Decimal("0.00") or v > Decimal("100.00"):
            raise ValueError("El avance debe estar entre 0.00 y 100.00.")
        return v

class SeguimientoCrearSchema(SeguimientoBaseSchema):
    id_proyecto: int
    observaciones: str
    id_usuario_responsable: int
    id_estado: int
    avance_porcentaje: Decimal


class SeguimientoRespuestaSchema(BaseModel):
    id_seguimiento_emprendimiento: int
    id_proyecto: int
    observaciones: str
    id_usuario_responsable: int
    fecha_registro: datetime
    id_estado: int
    avance_porcentaje: Decimal

    class Config:
        from_attributes = True

class SeguimientoActualizarSchema(SeguimientoBaseSchema):
    observaciones: Optional[str] = None
    id_usuario_responsable: Optional[int] = None
    id_estado: Optional[int] = None
    avance_porcentaje: Optional[Decimal] = None