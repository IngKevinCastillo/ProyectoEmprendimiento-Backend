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
    aspecto_revisado: Optional[str] = None
    id_mesas: Optional[int] = None
    transferir_mesa: Optional[bool] = None

    @field_validator("id_proyecto", "id_usuario_responsable", "id_estado", "id_mesas")
    @classmethod
    def validar_ids_positivos(cls, v: int, info: ValidationInfo) -> int:
        campo = info.field_name.replace("_", " ").capitalize()
        return validar_id_entero(v, campo=campo)

    @field_validator("observaciones", "aspecto_revisado")
    @classmethod
    def validar_observaciones(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        if not (20 <= len(v) <= 2000):
            raise ValueError(
                "Las observaciones deben tener entre 20 y 2000 caracteres.")
        return v

    @field_validator("avance_porcentaje")
    @classmethod
    def validar_avance(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        if v is None:
            return v
        v = Decimal(v)
        if not (Decimal("0.00") <= v <= Decimal("100.00")):
            raise ValueError("El avance debe estar entre 0.00 y 100.00.")
        if v.as_tuple().exponent < -2:
            raise ValueError("El avance solo puede tener hasta 2 decimales.")
        return v
    
    @field_validator("transferir_mesa")
    @classmethod
    def validar_transferir_mesa(cls, v: Optional[bool]) -> bool:
        if v is None:
            return v
        if not isinstance(v, bool):
            raise ValueError("El campo 'transferir_mesa' debe ser un valor booleano (true/false).")
        return v

class SeguimientoCrearSchema(SeguimientoBaseSchema):
    id_proyecto: int
    observaciones: str
    id_usuario_responsable: int
    id_estado: int
    avance_porcentaje: Decimal
    aspecto_revisado: str
    id_mesas: int
    transferir_mesa: bool = False


class SeguimientoRespuestaSchema(BaseModel):
    id_seguimiento_emprendimiento: int
    id_proyecto: int
    observaciones: str
    id_usuario_responsable: int
    fecha_registro: datetime
    id_estado: int
    avance_porcentaje: Decimal
    aspecto_revisado: Optional[str] = None
    id_mesas: int
    transferir_mesa: bool

    class Config:
        from_attributes = True

class SeguimientoActualizarSchema(SeguimientoBaseSchema):
    observaciones: Optional[str] = None
    id_usuario_responsable: Optional[int] = None
    id_estado: Optional[int] = None
    avance_porcentaje: Optional[Decimal] = None
    aspecto_revisado: Optional[str] = None
    id_mesas: Optional[int] = None
    transferir_mesa: Optional[bool] = None