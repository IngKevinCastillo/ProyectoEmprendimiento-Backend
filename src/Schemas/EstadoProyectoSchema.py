from pydantic import BaseModel, field_validator, condecimal
from datetime import datetime
from decimal import Decimal
from typing import Optional
from Utils.Validacionesutilidades import validar_descripcion

class EstadoProyectoBaseSchema(BaseModel):
    nombre_estado: str
    avance_porcentaje: Annotated[
        Decimal,
        Field(
            max_digits=5,
            decimal_places=2,
            ge=0,
            le=100
        )
    ]
    observaciones: Optional[str] = None
    id_usuario_responsable: int

    @field_validator("nombre_estado")
    @classmethod
    def validar_nombre_estado(cls, v: str) -> str:
        v = v.strip()
        if not (3 <= len(v) <= 30):
            raise ValueError("El nombre del estado debe tener entre 3 y 30 caracteres.")
        return v

    @field_validator("observaciones")
    @classmethod
    def validar_observaciones(cls, v: Optional[str]) -> Optional[str]:
        return validar_descripcion(v, min_len=20, max_len=2000, campo="Observaciones")

    @field_validator("id_usuario_responsable")
    @classmethod
    def validar_usuario(cls, v: int) -> int:
        if v < 1 or v > 2147483647:
            raise ValueError("El ID del usuario debe ser válido.")
        return v


class EstadoProyectoCrearSchema(EstadoProyectoBaseSchema):
    pass


class EstadoProyectoRespuestaSchema(BaseModel):
    id_estado_proyecto: int
    nombre_estado: str
    avance_porcentaje: Decimal
    observaciones: Optional[str]
    fecha_registro: datetime
    id_usuario_responsable: int

    class Config:
        from_attributes = True