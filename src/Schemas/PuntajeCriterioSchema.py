from pydantic import BaseModel, field_validator
from typing import Optional
from decimal import Decimal

class PuntajeCriterioCrearSchema(BaseModel):
    id_criterio: int
    nota: Decimal

    @field_validator("nota")
    @classmethod
    def validar_nota(cls, v: Decimal) -> Decimal:
        if v < 0 or v > 5:
            raise ValueError("La nota debe estar entre 0.0 y 5.0")
        return v

class PuntajeCriterioActualizarSchema(BaseModel):
    nota: Optional[Decimal] = None

    @field_validator("nota")
    @classmethod
    def validar_nota(cls, v: Decimal) -> Decimal:
        if v is not None and (v < 0 or v > 5):
            raise ValueError("La nota debe estar entre 0.0 y 5.0")
        return v

class PuntajeCriterioRespuestaSchema(BaseModel):
    id_puntaje: int
    id_evaluacion: int
    id_criterio: int
    nota: Decimal

    class Config:
        from_attributes = True